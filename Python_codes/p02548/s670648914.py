n=int(input())
cnt=0
for a in range(1,n):
    for b in range(1,n):
        if a*b <= n-1:
            cnt+=1
        else: break
print(cnt)