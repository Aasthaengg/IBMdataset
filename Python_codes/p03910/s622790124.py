n=int(input())

ans=[]
s=0
for i in range(1,n+1):
    s+=i
    ans.append(i)
    if s>=n:
        break

if s==n:
    for a in ans:
        print(a)
else:
    ans.remove((s-n))
    for a in ans:
        print(a)
