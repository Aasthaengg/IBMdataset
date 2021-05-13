s=input()
n=len(s)+1
a,b=[0]*n,[0]*n
temp=0
for i,val in enumerate(s):
    if val=="<": temp+=1
    else: temp=0
    a[i+1]=temp
temp=0
for i,val in enumerate(s[::-1]):
    if val==">": temp+=1
    else: temp=0
    b[n-i-2]=temp
ans=0
for i,j in zip(a,b): ans+=max(i,j)
print(ans)