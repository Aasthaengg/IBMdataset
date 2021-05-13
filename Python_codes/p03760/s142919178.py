o=list(input())
e=list(input())
n=len(o)
m=len(e)
ans=[]
for i in range(m):
    ans.append(o[i])
    ans.append(e[i])
if n!=m:
    ans.append(o[-1])
print("".join(ans))
