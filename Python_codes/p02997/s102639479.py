import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]

ans = []

for i in range(2, n + 1):
    ans.append([1, i])

dic2 = (n - 1) * (n - 2) // 2

if k > dic2:
    print(-1)
    sys.exit()

a = 2
b = 3
while k < dic2:
    ans.append([a, b])
    dic2 -= 1
    b += 1
    if b > n:
        a += 1
        b = a + 1
    if a >= n and dic2 > k:
        print(-1)
        sys.exit()
print(len(ans))
for i in ans:
    print(*i)

