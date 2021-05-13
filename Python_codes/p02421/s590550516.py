n = int(input())

tp = 0
hp = 0

for i in range(n):
    t, h = input().split()
    if t < h:
        hp += 3
    elif t > h:
        tp += 3
    elif t == h:
        tp += 1
        hp += 1

print('%d %d' % (tp, hp) )