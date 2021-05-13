N, K = map(int, input().split())
cnts = [0] * N
for n in range(K):
    d = int(input())
    A = list(map(int, input().split()))

    for a in A:
        cnts[a-1] += 1
cnt = 0
for c in cnts:
    if c == 0:
        cnt += 1
print(cnt)