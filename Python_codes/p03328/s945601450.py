a, b = map(int, input().split())

tmp = 0
for i in range(1, 499501):
    tmp += i
    if i == b-a: print(tmp-b)