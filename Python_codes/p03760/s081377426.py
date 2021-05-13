O=list(input())
E=list(input())
F=[]
if len(O)==len(E):
    for i in range(len(O)):
        F=F+[O[i]]+[E[i]]
else:
    for i in range(len(O)-1):
        F=F+[O[i]]+[E[i]]
    F+=O[len(O)-1]
print(''.join(F))