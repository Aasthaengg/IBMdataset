from collections import deque
S = input()
S  = deque(S)
Q = int(input())

# 0の時は普通、1の時は反転状態
Reverse_Flag = 0  

for _ in range(Q):
    string = (input())
    Query = string.replace(' ', '')
    Query = list(Query)

    if Query[0] == "1":
        if Reverse_Flag == 0:
            Reverse_Flag = 1
        else:
            Reverse_Flag = 0
    
    elif  Query[1] == "1":
        if Reverse_Flag == 0:
            S.appendleft(Query[2])
        else:
            S.append(Query[2])

    else:
        if Reverse_Flag == 0:
            S.append(Query[2])
        else:
            S.appendleft(Query[2])

if Reverse_Flag == 1:
    S = list(S)
    S = S[::-1]
    print("".join(S))
else:
    S = list(S)
    print("".join(S))
