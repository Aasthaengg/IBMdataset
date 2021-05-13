from sys import stdin
input = stdin.readline
N, D = map(int, input().split())

X=[0]*N
Y=[0]*N
c=0
for i in range(N):
    X[i], Y[i] = map(int, input().split())
    if D**2>=X[i]**2+Y[i]**2:c=c+1 

print(c)