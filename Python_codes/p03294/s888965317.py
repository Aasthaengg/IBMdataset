n=int(input())
arr=[int(i) for i in input().split()]
ans=0
for i in arr:
    ans+=(i-1)
print(ans)
