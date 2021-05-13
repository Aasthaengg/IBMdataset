#15 B - KEYENCE String
S = list(input())

result = 'NO'
for i in range(len(S)):
    Scpy = S.copy()
    for j in range(i,len(S)):
        Scond = Scpy[:i]+Scpy[j:]
        if (''.join(Scond)) == ('keyence'):
            result = 'YES'
            break
    else:
        continue
    break
print(result)