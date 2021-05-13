s = sum(map(int, input().split()))

d, m = divmod(s, 2)
if m != 0:
    d += 1
print(d)
