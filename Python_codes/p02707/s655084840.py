n=int(input())
a=[int(j)for j in input().split()]
b=[0]*int(n)
for i in a:
    b[int(i)-1]+=1
print(*b)