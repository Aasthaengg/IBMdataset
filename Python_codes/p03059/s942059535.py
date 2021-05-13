A, B, T = [int(n) for n in input().split()]

t = 0
m = 0
while(1):
    t += A
    if t <= T + 0.5:
        m += B
    else:
        break


print(m)