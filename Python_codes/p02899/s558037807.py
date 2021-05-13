n=int(input())
a=[int(i)for i in input().split()]
res=[0 for i in range(n)]
for i in range(n):
    res[a[i]-1]=i+1
print(" ".join(map(str,res)))