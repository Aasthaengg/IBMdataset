s = input()
t = 'CODEFESTIVAL2016'
a = sum(c1 != c2 for c1, c2 in zip(s, t))
print(a)