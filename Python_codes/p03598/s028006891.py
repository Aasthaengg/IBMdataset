N = int(input())
K = int(input())
X = list(map(int,input().split()))
cnt = 0
for i in range(N):
    cnt += min(X[i],K-X[i])
print(2*cnt)