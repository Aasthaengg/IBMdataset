import collections
def main():

    N, W = map(int, input().split())
    goods = collections.defaultdict(list)
    for _ in range(N):
        w, v = map(int, input().split())
        goods[w].append(v)

    for w in goods:
        goods[w].sort(reverse = True)

    cur = dict()
    cur[0] = 0
    for w in goods:
        temp = cur.copy()
        for w1 in temp:
            w2, v2 = w1, temp[w1]
            for i in range(len(goods[w])):
                w2 += w
                v2 += goods[w][i]
                if w2 <= W:
                    if w2 not in cur:
                        cur[w2] = v2
                    else:
                        cur[w2] = max(cur[w2], v2)
    max_v = 0
    for w in cur:
        max_v = max(max_v, cur[w])
    return max_v

if __name__ == '__main__':
    print(main())