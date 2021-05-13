o = input()
e = input()
s = ''.join([o[i//2] if i % 2 == 0 else e[i//2] for i in range(len(o)+len(e))])
print(s)