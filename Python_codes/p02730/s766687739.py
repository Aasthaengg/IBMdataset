S = input()

def kaibun(x):
    N = len(x)
    flag = True
    for i in range(N // 2):
        if x[i] != x[-i - 1]:
            flag = False
    return flag

tmp1 = kaibun(S)
tmp2 = kaibun(S[:(len(S) - 1) // 2])
tmp3 = kaibun(S[(len(S) + 3) // 2 - 1:])


if tmp1 and tmp2 and tmp3:
    print('Yes')
else:
    print('No')


        
