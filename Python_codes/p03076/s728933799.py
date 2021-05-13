a = [int(input()) for _ in range(5)]

t = 0

m = 10

for x in a:
    t += (x + 9) // 10 * 10
    m = min((x - 1) % 10 + 1, m)

print(t-10+m) 