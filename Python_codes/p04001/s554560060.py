def RecSum(S, i):
    if i > len(S) - 1:
        return eval(''.join(S))
    SS = S.copy()
    SS.insert(i, "+")
    return RecSum(S, i+1) + RecSum(SS, i+2)


S = list(input())
print(RecSum(S, 1))
