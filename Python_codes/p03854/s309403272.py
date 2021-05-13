S = input ()
Z = ''.join(list(reversed(S)))
Z = Z.replace('resare', '')
Z = Z.replace('esare', '')
Z = Z.replace('remaerd', '')
Z = Z.replace('maerd', '')
z = len (Z)
if z == 0:
    print ('YES')
else:
    print ('NO')