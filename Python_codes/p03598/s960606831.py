import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
X = list(map(int,input().split()))
count = 0
for i in range(N):
    count += min(X[i],abs(K-X[i])) * 2
print(count)
