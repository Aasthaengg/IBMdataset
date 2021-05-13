N = int(input())
X = list(map(int, input().split()))
ans = 1<<60
for center in range(101):
    a = 0
    for x in X:
        a += (x - center) ** 2
    if a < ans:
        ans = a
print(ans)
