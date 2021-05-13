N, K = map(int, input().split())
A = [int(a) for a in input().split()]

p = 10**9 + 7

all = 0
aft = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            all += 1
            if i < j:
                aft += 1

print((all * K * (K-1)//2 + K * aft) % p)
