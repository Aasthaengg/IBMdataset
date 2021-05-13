n = int(input())
a = list(map(int, input().split()))

xor = a[0]
for i in range(1, n):
    xor ^= a[i]

ans = []
for elem in a:
    ans.append(elem ^ xor)

print(*ans)