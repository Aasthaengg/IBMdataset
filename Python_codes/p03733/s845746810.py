n,t=map(int,input().split())
T=list(map(int,input().split()))
cur=0
sho=0
for i in range(n-1):
    cur=T[i]
    if cur+t<T[i+1]:
        sho+=t
        cur=T[i+1]
    else:
        sho+=T[i+1]-cur
        cur=T[i+1]
print(sho+t)