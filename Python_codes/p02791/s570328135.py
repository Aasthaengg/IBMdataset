N = int(input())
P = [int(s) for s in input().split()]

cnt = 0
min_val = 10 ** 8
for p in P:
    if p <= min_val:
        min_val = p
        cnt += 1

print(cnt)