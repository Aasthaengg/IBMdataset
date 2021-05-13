N=int(input())
A,B=map(int,input().split())
P=[int(i) for i in input().split()]

x = len([0 for i in P if i<=A])
y = len([0 for i in P if i>=A+1 and i<=B])
z = len([0 for i in P if i>=B+1])

print(min(min(x,y),z))