s=input()
t=input()
n=len(s)
f=0
if s==t:
    f=1
for i in range(n):
    ans=0
    for j in range(i):
        
        if s[n+j-i]==t[j]:
            ans+=1
    for j in range(n-i):
        
        if s[j]==t[i+j]:
            
            ans+=1
    if ans==n:
        f=1
    
print("Yes" if f==1 else "No")
            

    
