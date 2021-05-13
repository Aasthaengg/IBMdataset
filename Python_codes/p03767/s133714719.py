n = int(input())
a = [int(i) for i in input().split()]

a.sort()
ans=0
for i in a[n::2]:
    ans+=i
print(ans)
