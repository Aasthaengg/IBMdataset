def solve(n, a):
    S, T = {}, {}
    for i in range(n):
        b = a[i] + i
        if not b in S:
            S[b] = 0
        S[b] += 1

        c = -a[i] + i
        if not c in T:
            T[c] = 0
        T[c] += 1
    ans = 0
    for x, num in S.items():
        if x in T:
            ans += S[x] * T[x]
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))