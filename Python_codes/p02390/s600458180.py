S = int(input())
m, s = divmod(S, 60)
h, m = divmod(m, 60)
print(h, m, s, sep=':')
