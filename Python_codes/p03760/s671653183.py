o = list(str(input()))
x = list(str(input()))
ln = []
for i in range(len(o)):
    ln.append(o[i])
    if len(x) > i:
        ln.append(x[i])
print(''.join(ln))