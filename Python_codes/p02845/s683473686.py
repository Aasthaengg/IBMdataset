n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
data = [0, 0, 0]
ans = 1
for x in a:
    y = 0
    t = True
    for i in range(3):
        if data[i] == x:
            y += 1
            if t:
                t = False
                data[i] += 1
    ans *= y
    ans %= mod

print(ans)
