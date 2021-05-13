n = list(str(input()))
x = ['1' if i=='9' else '9' for i in n]
print(''.join(x))
