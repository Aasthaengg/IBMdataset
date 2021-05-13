N = int(input())
A = [int(input()) for _ in range(5)]
a = min(A)
n = N//a
k = N%a
ans = 0
if n>0:
    ans = 5+(n-1)
    if k>0:
        ans += 1
else:
    if k>0:
        ans = 5
print(ans)