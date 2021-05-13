x, y, val = map(int, raw_input().split())
res = 0
for i in range(x, y+1):
    if val % i == 0:
        res += 1
print res