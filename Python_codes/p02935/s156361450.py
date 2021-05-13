N = int(input())
V = sorted(list(map(int, input().split())), reverse=True)

for _ in range(N-1):
    x = V.pop()
    y = V.pop()
    V.append((x + y) / 2)
    V.sort(reverse=True)
print(*V)
