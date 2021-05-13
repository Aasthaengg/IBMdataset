s = input()[::-1]
r = 'YES'
while len(s):
    if s[:5] == 'dream'[::-1] or s[:5] == 'erase'[::-1]:
        s = s[5:]
    elif s[:6] == 'eraser'[::-1]:
        s = s[6:]
    elif  s[:7] == 'dreamer'[::-1]:
        s = s[7:]
    else:
        r = 'NO'
        break
print(r)