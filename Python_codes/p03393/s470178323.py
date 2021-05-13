s = input()
c = len(s)-1
r = 0
x = 97
while -2 < c:
    for i in range(x, 97+26):
        if chr(i) not in s:          
            s = s+chr(i)
            r = 1
            break
    if r == 1:
        break
    elif c < 0:
        break
    else:
        x = ord(s[-1]) +1
        c -= 1
        s = s[:len(s)-1]
if r==0:
    s = '-1'
print(s)