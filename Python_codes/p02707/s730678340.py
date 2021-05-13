N = int(input())
A = list(map(int, input().split()))

cnt = [0] * N
for i in range(N-1):
    cnt[A[i] - 1] += 1

print(*cnt, sep='\n')
