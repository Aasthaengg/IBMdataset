a,b = input().split()
c = ['H','D']
c.remove(b)

if a =='H':
    print(b)
else:
    print(*c)