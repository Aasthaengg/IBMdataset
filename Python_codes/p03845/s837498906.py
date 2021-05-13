N = int(input())
T = list(map(int,input().split()))
M = int(input())
P = [0]*M
X = [0]*M
for i in range(M):
    P[i],X[i] =map(int,input().split())
Sum = sum(T)
for i in range(M):
    print(Sum-(T[P[i]-1]-X[i]))