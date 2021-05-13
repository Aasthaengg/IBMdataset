s = input()
n = int(input())
methods = {'print': lambda s, b, e: (s, print(s[b:e+1])),
           'reverse': lambda s, b, e: (s[:b] + s[e:b-len(s)-1:-1] + s[e+1:],),
           'replace': lambda s, b, e, r: (s[:b] + r + s[e+1:],)}
for _ in range(n):
    args = input().split(' ')
    method = args[0]
    args[1] = int(args[1])
    args[2] = int(args[2])
    s = methods[method](s, *args[1:])[0]