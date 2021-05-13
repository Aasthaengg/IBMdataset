n=int(input())
a=[int(j)for j in input().split()]
x=0
for i in a:x^=i
print(*[x^i for i in a])