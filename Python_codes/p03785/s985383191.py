n,c,k=map(int,input().split())
t=[int(input()) for _ in range(n)]
t.sort()
cnt,now=0,0
while now<n:
    temp=t[now]+k
    a=now
    for i in range(c-1):
        if i+1+a>=n:
            break
        if t[i+1+a]>temp:
            break
        now+=1
    now+=1
    cnt+=1
print(cnt) 