from copy import deepcopy
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    l = [2,5,5,4,5,6,3,7,6]
    d = {}
    for i in A:
        if l[i-1] not in d:
            d[l[i-1]] = i
        else:
            if d[l[i-1]] < i:
                d[l[i-1]] = i
    d3 = {}
    for i in d:
        d3[d[i]] = i
    d2 = list(d)
    d2.sort()
    s = [[[-1] * (len(d2)) for _ in range(len(d2))] for _ in range(N+1)]
    dp = [[0] * (len(d2)) for _ in range(N+1)]
    for w in range(N+1):
        if w % d2[0] == 0:
            dp[w][0] = w // d2[0]
            s[w][0] = [0] * (len(d2))
            s[w][0][0] = w // d2[0]
    for i in range(1, len(d2)):
        for w in range(N+1):
            if w < d2[i]:
                continue
            elif max(dp[w-d2[i]]) > 0:
                x = dp[w-d2[i]].index(max(dp[w-d2[i]]))
                if dp[w][i-1] > dp[w-d2[i]][x] + 1:
                    dp[w][i] = dp[w][i-1]
                    s[w][i] = deepcopy(s[w][i-1])
                else:
                    dp[w][i] = dp[w-d2[i]][x] + 1
                    s[w][i] = deepcopy(s[w-d2[i]][x])
                    s[w][i][i] += 1
            elif w == d2[i]:
                dp[w][i] = 1
                s[w][i] = [0] * len(d2)
                s[w][i][i] = 1
            else:
                dp[w][i] = dp[w][i-1]
                s[w][i] = deepcopy(s[w][i-1])
    maxn = 0
    for i in s[-1]:
        if sum(i) <= 0:
            continue
        qq = []
        for j,v in enumerate(i):
            if v > 0:
                qq.append((d[d2[j]],v))
        qq.sort(key=lambda x:x[0], reverse=True)
        r = ''
        for k in qq:
            r += str(k[0]) * k[1]
        if int(r) > maxn:
            maxn = int(r)
    print(maxn)
main()
