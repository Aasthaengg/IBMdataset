n=int(input())
ans=0
if 10**(len(str(n))-1)==n:
    ans=10
else:
    listn=list(str(n))
    for i in range(len(listn)):
        ans+=int(listn[i])
print(ans)
