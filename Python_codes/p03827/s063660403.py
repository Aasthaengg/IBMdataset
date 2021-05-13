n = int(input())
s = input()

res = 0
x = 0
for i, v in enumerate(s):
    if v == 'I':
        x += 1
    else:
        x -= 1
    res = max(res, x)
print(res)
