n, k = map(int,input().split())
A = list(map(int,input().split()))

ans = float('inf')
for i in range(n-k+1):
    left = A[i]
    right = A[i+(k-1)]
    if right <= 0:
        ans = min(ans, abs(left))
    elif 0 <= left:
        ans = min(ans, right)
    else:
        tmp1 = 2*abs(left)+right
        tmp2 = 2*right+abs(left)
        ans = min(ans, min(tmp1, tmp2))
print(ans)