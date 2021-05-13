def nC2(n):
    return n*(n-1)//2


N = int(input())
A = list(map(int, input().split()))
combi = {}

for i in A:
    try:
        combi[i] += 1
    except KeyError:
        combi[i] = 1

total = sum(nC2(i) for i in combi.values())

for i in range(N):
    ans = total - nC2(combi[A[i]])
    ans += nC2(combi[A[i]] - 1)
    print(ans)
