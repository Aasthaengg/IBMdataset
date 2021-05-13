n ,m = map(int, input().split())
a = list(map(int,input().split()))
ans = 0
refer = sum(a) / (4*m)

for ni in range(n):
    if a[ni] >= refer:
        ans += 1

if ans >= m:
    print('Yes')
else:
    print('No')