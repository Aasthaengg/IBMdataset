n=int(input())
k=int(input())
ans=1
for i in range(n):
    multi=ans*2
    add=ans+k
    ans=min(multi,add)
print(ans)