n = int(input())
ans1 = ans2 = 0
for _ in range(n):
    a, b = map(int, input().split())
    if ans1 < a:
        ans1 = a
        ans2 = b
print(ans1 + ans2)
