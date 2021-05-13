n = int(input())
A = list(map(int,input().split()))

ans = 1
d = 0
for i in range(1,n):
    diff = A[i] - A[i-1]
    if not d:
        d = diff
    elif d*diff < 0:
        d = 0
        ans += 1
print(ans)