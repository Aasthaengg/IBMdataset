O = list(input())
E = list(input())
Ans = []
for i in range(len(O + E)):
    if i % 2 == 0:
        Ans.append(O[i // 2])
    else:
        Ans.append(E[i // 2])
print(''.join(Ans))
