n=int(input())
ans=[]
sm=0
for i in range(1,n+1):
    sm+=i
    ans.append(i)
    if sm==n:
        break
    if sm>n:
        p=sm-n
        ans.pop(p-1)
        break

for i in ans:
    print(i)