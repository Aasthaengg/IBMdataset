n,k = map(int,input().split())

cnt = 0
for b in range(k+1,n+1):
    l = n//b
    if k == 0:
        cnt += n
    else:
        cnt += (b-k)*l + max(0,(n-b*l) - (k-1) )
print(cnt)
