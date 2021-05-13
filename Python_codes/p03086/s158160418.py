s=input()
n=len(s)
a=["A","G","C","T"]
f=0
m=0
ans=0
for i in range(n):
    if f==0:
        if s[i] in a:
            ans+=1
            f=1
    elif f==1:
        if s[i] in a:
            ans+=1
        else:
            m=max(ans,m)
            f=0
            ans=0
m=max(ans,m)
print(m)
            
    
