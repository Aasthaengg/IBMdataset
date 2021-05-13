N = int(input())
A = list(map(int, input().split()))
r = 0
for a in A:
    t = a
    while True:
        if t % 2 == 1:
            break
        t = t / 2
        r += 1
print(r)
