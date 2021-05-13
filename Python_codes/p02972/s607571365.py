#coding: utf-8
N = int(input())
A = [0] + list(map(int, input().split()))
B = [0 for _ in range(N+1)]
ans = []
for i in range(N, 0, -1):
    v = 0
    j = i
    while j <= N:
        v += B[j]
        j += i
    if A[i] != v % 2:
        ans.append(i)
        B[i] = 1

ans.sort()
print(len(ans))
if len(ans) != 0:
    print(*ans)