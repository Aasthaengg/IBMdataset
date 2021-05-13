n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = 10**13
for i in range(n-k+1):
    left = l[i]
    right = l[k+i-1]
    if right <= 0:
        time = abs(left)
    elif 0 <= left:
        time = abs(right)
    else:
        time = min(abs(left),abs(right))*2 + max(abs(left),abs(right))
    ans = min(ans,time)
print(ans)