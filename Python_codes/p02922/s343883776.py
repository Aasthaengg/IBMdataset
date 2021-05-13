import sys
a, b = map(int, input().split())
c = 0
s = 1

if b == 1:
    print(0)
    sys.exit()

while True:
    for e in range(s):
        c += 1
        s = s - 1 + a
        if s >= b:
            print(c)
            break
    else:
        continue
    break
