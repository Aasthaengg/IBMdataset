N = int(input())
P = list(reversed(list(map(int, input().split()))))

s, t = 2, 2
for i in P:
    p = max((s + i - 1) // i, 1)
    q = t // i
    if q < p:
        print(-1)
        quit(0)
    s, t = p * i, q * i + i - 1

print(s, t)
