L, R = map(int, input().split(' '))

N = 2019


ans = 2019

for i in range(L, R):
    for j in range(i + 1, R + 1):
        mod = (i * j) % N
        if ans > mod:
            ans = mod
        if ans == 0:
            print(ans)
            exit(0)

print(ans)