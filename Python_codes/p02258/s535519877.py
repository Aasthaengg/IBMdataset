# encoding=utf-8
n = int(raw_input())

min = int(raw_input())
diff = -1000000000
n = n - 1

for i in range(n):
    v = int(raw_input())

    if v - min > diff:
        diff = v - min
    if min > v:
        min = v

print diff