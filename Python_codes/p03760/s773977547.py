o=input()
e=input()
n=len(e)
ans=""
for i in range(n):
    ans+=o[i]
    ans+=e[i]
if len(o)>n:
    ans+=o[-1]
print(ans)