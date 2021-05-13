n=int(input())
x=[int(i)for i in input().split()]
p=[sum([(j-i)**2 for j in x]) for i in range(101)]
print(min(p))