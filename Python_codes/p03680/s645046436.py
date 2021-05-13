n=int(input())
ans=0
result=0
s=[]
for _ in range(n):
    s.append(int(input()))
    
pos=s[0]

for i in range(n):
    if pos==2:
        ans+=1
        result+=1
        break
    else:
        pos=s[pos-1]
        ans+=1

if result==0:
    print(-1)
else:
    print(ans)