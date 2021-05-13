a,b,k=map(int,input().split())

c=min(a,b)
d=max(a,b)
ans=[]

for i in range(c):
    if c%(i+1)==0 and d%(i+1)==0:
        ans.append(i+1)
            
print(ans[-k])