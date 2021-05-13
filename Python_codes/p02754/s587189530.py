n, a, b = map(int, input().split())
q, mod = divmod(n, a+b)
print(a*q+mod if mod<=a else a*q+a)