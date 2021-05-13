n = int(input())
As = list(map(int, input().split()))

a = max(As)

# 一番a/2に近い数を選ぶ
b = None
dist = float('inf')
for i in range(n):
    if As[i] != a and abs(As[i] - a/2) < dist:
        dist = abs(As[i] - a/2)
        b = As[i]

print(a, b)
