n = int(input())
p = [int(s) for s in input().split()]

diff = 0
for i in range(n):
    if p[i] != i + 1:
            diff += 1
print('YES') if diff <= 2 else print('NO')