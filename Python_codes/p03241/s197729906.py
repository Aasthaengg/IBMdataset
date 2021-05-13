def divisor(x):
    d = []
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            d.append(i)
            if i!=(x//i): d.append(x//i)
    d.sort()
    return d

n, m = map(int, input().split())
d = divisor(m)
for i in range(len(d)-1, -1, -1):
    if d[i] <= m/n:
        print(d[i])
        break