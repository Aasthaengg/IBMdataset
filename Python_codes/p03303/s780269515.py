s=list(input())
n=int(input())
ans=[]
m=len(s)//n
if len(s)%n!=0:
    m+=1
for i in range(m):
    ans.append(s[n*i])
print(''.join(ans))


