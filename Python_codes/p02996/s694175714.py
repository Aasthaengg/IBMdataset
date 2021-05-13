import sys
N = int(input())
a, b = [], []
ans = 0

for i in range(N):
    a0, b0 = map(int, input().split())
    a.append(a0)
    b.append(b0)
b, a = zip(*sorted(zip(b, a)))
for i, j in zip(a, b):
    ans += i
    if ans > j:
        print('No')
        sys.exit()
print('Yes')
