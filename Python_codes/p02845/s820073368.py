n = int(input())
a = list(map(int, input().split()))

mod = 1000000007
ans = 1
rgb = [0, 0, 0]
for num in a:
    ans = (ans * rgb.count(num)) % mod
    if ans == 0:
        break
    index = rgb.index(num)
    rgb[index] += 1
print(ans)