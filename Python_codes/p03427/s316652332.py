N = input()

# NはK桁
K = len(N)

# 最上位の桁がc
c = int(N[0])

# 最上位の桁以外
d = N[1:]

if "9" * len(d) == d:
    print(c + 9 * (K - 1))
else:
    print(c + 9 * (K - 1) - 1)
