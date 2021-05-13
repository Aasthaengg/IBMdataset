N = int(input())
A = list(map(int, input().split()))
a = 0
for i in range(N):
    if A[i] % 2 == 0:
        a += 1
ans = 3 ** N - 2 ** a
print(ans)