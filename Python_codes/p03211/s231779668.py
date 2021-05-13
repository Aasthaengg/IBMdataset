s=list(input())
n=len(s)
ans=0
m=1000
for i in range(n-2):
    ans=100*int(s[i])+10*int(s[i+1])+int(s[i+2])
    m=min(m,abs(ans-753))
print(m)
    
