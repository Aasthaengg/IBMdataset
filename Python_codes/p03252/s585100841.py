S=list(input())
T=list(input())

from collections import Counter
Counter_S=Counter(S)
Counter_T=Counter(T)
S_num=list(Counter_S.values())
T_num=list(Counter_T.values())

S_num.sort()
T_num.sort()

if S_num==T_num:
    print('Yes')
else:
    print('No')