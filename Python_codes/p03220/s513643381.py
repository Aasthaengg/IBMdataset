N = int(input())
T, A = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
diff = float("inf")

for i, height in enumerate(h):
    temp = T - 0.006 * height
    if diff > abs(A - temp):
        diff = abs(A - temp)
        ans = i + 1

print(ans)
