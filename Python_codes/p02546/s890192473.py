n = input()
n = [ c for c in n]
if(n[-1]=='s'):
    n.append('es')
elif(n[-1]!='s'):
    n.append('s')
n=''.join(n)
print(n)


