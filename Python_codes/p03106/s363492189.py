a, b, k = map(int, input().split())
ans = 0
for i in range(100):
    if a % (100-i) == 0 and b % (100-i) == 0:
        k -= 1
    if k == 0:
        ans = 100 - i
        print(ans)
        break