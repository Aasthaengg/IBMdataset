N,x=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)
cnt=0
for i in range(N):
    if sum(a)==x:
        cnt=N
    elif sum(a)>x:
        if x>=a[i]:
            x-=a[i]
            cnt+=1
        else:
            break
    else:
        cnt=N-1

print(cnt)