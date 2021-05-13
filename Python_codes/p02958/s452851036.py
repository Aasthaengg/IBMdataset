n = int(input())
p = list(map(int, input().split()))
c = 0
for i in range(0, n):
    if p[i] != i + 1:
        c += 1
print("YES" if c <= 2 else "NO")