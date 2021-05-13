a = list(map(str, input()))+['a']
b = list(map(str, input()))+['b']
c = list(map(str, input()))+['c']
now = 'a'
ans = 'A'
while len(a) != 0 and len(b) != 0 and len(c) != 0:
    if now == 'a':
        now = a[0]
        a.pop(0)
        ans = 'A'
    elif now == 'b':
        now = b[0]
        b.pop(0)
        ans = 'B'
    else:
        now = c[0]
        c.pop(0)
        ans = 'C'
print(ans)
    
