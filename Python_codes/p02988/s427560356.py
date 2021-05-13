n=int(input())
a=[int(i) for i in input().split()]
ans=0

for i in range(n-2):
    if sorted(a[i:i+3])[1]==a[i:i+3][1]:
        ans+=1
print(ans)