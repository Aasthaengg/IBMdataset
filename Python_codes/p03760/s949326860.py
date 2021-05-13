o = input()
e = input()
l =len(o)+len(e)
p = []
for i in range(l):
    if i % 2 == 0:
        p.append(o[i//2])
    else:
        p.append(e[i//2])
        
print(''.join(p))