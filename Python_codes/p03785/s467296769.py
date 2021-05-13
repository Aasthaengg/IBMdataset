n,c,k=map(int,input().split())
t=[int(input()) for _ in range(n)]
t.sort()
ans=0
num=0
for i in range(n+3):
    if num>=n:
        break
    num2=t[num]+k
    ans+=1
    for j in range(c-1):
        num+=1
        if num==n:
            break
        if t[num]>num2:
            num-=1
            break
    num+=1
print(ans)
