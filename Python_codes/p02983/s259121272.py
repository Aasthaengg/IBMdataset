import sys
L, R = map(int, input().split())
N, val = 2019, 2019

for i in range(L, R):
    for j in range(i+1, R+1):
        mod = (i * j) % N
        if val > mod:
            val = mod
        if val == 0:
            print(val)
            sys.exit()
print(val)
