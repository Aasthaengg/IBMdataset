s=input().strip()

n = 0
for c in list(s):
    if c == '+':
        n += 1
    elif c == '-':
        n -= 1
print(n)
