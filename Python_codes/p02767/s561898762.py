n=int(input())
x=[int(i)for i in input().split()]
p=[0 for i in range(101)]
for i in range(101):
    p[i]=sum([(j-i)**2 for j in x])
print(min(p))