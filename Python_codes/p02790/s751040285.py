a, b = map(int,input().split())

c = max(a, b)
d = min(a, b)

print(''.join([str(d) for i in range(c)]))
