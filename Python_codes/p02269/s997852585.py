n = int(input())
  
l = []
s = {}
for i in range(n):
    c, m = input().split()
    if c[0] == 'i':
        s[m] = 0
    elif c[0] == 'f':
        if m in s:
            l.append('yes')
        else:
            l.append('no')
print(*l,sep='\n')