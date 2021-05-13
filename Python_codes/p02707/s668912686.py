N = int(input())
A = list(map(int,input().split()))
li = [0] * N
for i in range(N - 1): li[A[i] - 1] += 1
for i in range(N): print(li[i])