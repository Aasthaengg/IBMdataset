mii = lambda: map(int, input().split())

N = int(input())
pair = []
for i in range(N):
    a, b = mii()
    pair.append((a, b))
pair.sort()
print(pair[-1][0] + pair[-1][1])
