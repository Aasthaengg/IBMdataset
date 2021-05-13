N = int(input())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))


AB = sorted(AB, key=lambda x: x[0])
print(AB[-1][0] + AB[-1][1])
