a,b = map(int, input().split())
n = 0
t = 1
while True:
    if t >= b:
        break
    n += 1
    t += a-1
print(n)
