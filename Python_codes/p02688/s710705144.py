N, K = map(int, input().split())
okasi = [1] * N

for k in range(K):
    d = int(input())
    S = list(map(int, input().split()))
    for s in S:
        okasi[s - 1] = 0

print(sum(okasi))