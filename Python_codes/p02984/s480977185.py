import sys
N = int(sys.stdin.readline().rstrip())
D = list(map(int, sys.stdin.readline().rstrip().split()))
D_sum = 0 
D_sum_gusu = 0

for i, d in enumerate(D, 1):
    D_sum += d
    if i % 2 == 0:
        D_sum_gusu += d

ans = []

r = D_sum - 2 * D_sum_gusu
ans.append(r)
for d in D[:-1]:
    r = 2 * d - r
    ans.append(r)

print(" ".join(map(str, ans)))