n,k = map(int,input().split())
cnt = 0
for b in range(1,n+1):
    p = n//b
    r = n%b
    cnt += max(0, b-k)*p + max(0, r-k+1)
else:
    if k==0:
        cnt -= n
print(cnt)