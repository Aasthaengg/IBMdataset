N=int(input())
A,B=map(int,input().split())
P=[int(i) for i in input().split()]

print(min(len([p for p in P if p<=A]), \
len([p for p in P if A+1<=p<=B]), \
len([p for p in P if B+1<=p])))