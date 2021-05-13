N = int(input())

p_ = list(range(1, N+1))
p = [int(n) for n in input().split()]

count = 0
for i in range(N):
    if p_[i] != p[i]:
        count += 1

if count <= 2:
    print('YES')
else:
    print('NO')
