blue = [input() for _ in range(int(input()))]
red = [input() for _ in range(int(input()))]
ans = 0
for i in set(blue):
    c= blue.count(i) - red.count(i)
    ans = max(c, ans, 0)
print(ans)