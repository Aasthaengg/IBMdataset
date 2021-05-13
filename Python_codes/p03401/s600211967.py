N=int(input())
X = [0]+list(map(int,input().split()))+[0]
SUMX = 0
for i in range(1,len(X)):
    SUMX += abs(X[i-1] - X[i])
for i in range(1,N+1):
    print(SUMX + abs(X[i-1] - X[i+1]) - abs(X[i] - X[i-1]) - abs(X[i+1] - X[i]))