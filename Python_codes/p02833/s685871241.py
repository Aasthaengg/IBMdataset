def wtf(x):
    twos = 0
    fives = 0
    for j in range(1, 60):
        bs = 2 ** j
        twos = twos + x // bs
        bs = 2 * 5 ** j
        fives = fives + x // bs
    return min(twos, fives)
x = int(input())
print(wtf(x) if x % 2 == 0 else 0)