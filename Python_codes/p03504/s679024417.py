import collections
def main():

    N, C = map(int, input().split())
    d = collections.defaultdict(list)

    for _ in range(N):
        s, t, c  = map(int, input().split())
        d[c].append([s, t])

    for c in d:
        d[c].sort()
        lv = []
        for i in range(len(d[c])):
            if i == 0:
                lv.append(d[c][i])
            else:
                if lv[-1][1] == d[c][i][0]:
                    lv[-1][1] = d[c][i][1]
                else:
                    lv.append(d[c][i])
        d[c] = lv

    # print(d)
    index = dict()
    for c in d: index[c] = 0
    bound = max([d[c][-1][1] for c in d])
    ans = 0
    for i in range(1, bound + 1):
        cnt = 0
        for c in d:
            while index[c] < len(d[c]) and d[c][index[c]][1] < i:
                index[c] += 1
            if index[c] < len(d[c]) and d[c][index[c]][0] <= i <= d[c][index[c]][1]:
                cnt += 1
        # print(i, cnt)
        ans = max(ans, cnt)
    return ans


if __name__ == '__main__':
    print(main())