from math import floor
from decimal import Decimal

S = list(input())
T = list(input())

isSuccess = False

for i in reversed(range(len(S) - len(T) + 1)):
    T_str = S[i: i + len(T)]
    for j in range(len(T)):
        if T_str[j] != T[j] and T_str[j] != "?":
        	break
    else:
        isSuccess = True
        S[i:i + len(T)] = T
        break
if isSuccess == False:
    print("UNRESTORABLE")
else:
    string = ",".join(S)
    string = string.replace('?', 'a')
    S = string.split(',')
    print("".join(map(str,S)))