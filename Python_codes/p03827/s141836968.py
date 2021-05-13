n = int(input())
s = input()

res = 0
v = 0
for c in s:
    if c == 'I':
        v += 1
    else:
        v -= 1
    res = max(res, v)

print(res)