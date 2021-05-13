import sys
input = sys.stdin.readline

a, b, c, x = [int(input()) for i in range(4)]

n = 0
for an in range(a+1):
    for bn in range(b+1):
        for cn in range(c+1):
            if 500 * an + 100 * bn + 50 * cn == x:
                n += 1
print(n)