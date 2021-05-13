N = int(input())
A = [int(s) for s in input().split()]

cnt = 0
target = 1
for a in A:
    if a == target:
        cnt += 1
        target += 1

print(N - cnt if target != 1 else -1)