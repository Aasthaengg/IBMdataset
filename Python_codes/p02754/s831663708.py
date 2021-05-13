n, a, b = map(int, input().split())

q, mod = divmod(n, (a+b))
if mod > a:
    print(q*a+a)
else:
    print(q*a+mod)