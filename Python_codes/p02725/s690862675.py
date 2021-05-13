K, N = map(int, input().split())
A = list(map(int, input().split()))

#0と最後
max_ = [0, K+A[0]-A[-1]]

#iとi+1
for i in range(1, N):
    tmp = A[i] - A[i-1]
    if tmp > max_[1]:
        max_[0] = i
        max_[1] = tmp
print(K-max_[1])