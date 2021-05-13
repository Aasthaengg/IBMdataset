a = []
while 1:
    n = input()
    if n == '0 0':
        break
    a.append(n)
for s in a:
    x, y = map(int, s.split())
    print(f'{y} {x}') if x > y else print(s)
