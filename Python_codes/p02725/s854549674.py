K, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

A = A + [K]

lis = [0]*N
for i in range(N):
    lis[i] = A[i+1] - A[i]

#一番長い距離を引くか, 端から端までか
print(min(sum(lis[:N-1]), K - max(lis)))