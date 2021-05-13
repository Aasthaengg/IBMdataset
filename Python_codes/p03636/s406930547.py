s=list(input())

L=[s[0]]
L.append(str(len(s)-2))
L.append(s[-1])
print(''.join(L))