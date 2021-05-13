O = list(input())
E = list(input())

ans = list()
for i in range(max(len(O),len(E))):
    try:
        ans.extend([O[i],E[i]])
    except IndexError:
        if len(O) > len(E):
            ans.extend(O[i])
        else:
            ans.extend(E[i])
print(''.join(ans))
