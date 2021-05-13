n=int(input())
a=[x for x in input().split()]
ans=[0]*n
for i in range(n):
    ans[int(a[i])-1] = i+1
    
print(*ans)