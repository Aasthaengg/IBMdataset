n = int(input())
  
s = set()
for i in range(n):
    c, m = input().split()
    if c[0] == 'i':
        s.add(m)
    elif c[0] == 'f':
        if m in s:
            print('yes')
        else:
            print('no')