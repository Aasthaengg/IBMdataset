N = int(input())
A = list(map(int, input().split()))

A_i = [A[i] - i - 1 for i in range(N)]
A_i.sort()
b = A_i[N // 2]
ans = 0
for a in A_i:
    ans += abs(a - b)

print(ans)
