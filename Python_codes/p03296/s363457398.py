n =int(input())
A =list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(n-1):
    if A[i] == A[i+1]:
        A[i+1] = 101 + ans
        ans += 1
print(ans)
