n=int(input())
r=int(n**0.5)
ans=1
for i in range(r+1):
    if i**2>ans:
        ans=i**2
print(ans)