n=int(input())
if n==0:
    print(0)
    exit()
ans=[]
while n!=0:
    n,mod=divmod(n,-2)
    if mod==-1:
        mod=1
        n+=1
    ans.append(mod)
ans.reverse()
print("".join(map(str,ans)))