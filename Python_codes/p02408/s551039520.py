a = int(input())
b = []
S = []
H = []
C = []
D = []
check = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(a):
    b.append(input().split())
for i in range(len(b)):
    if b[i][0] == "S":
        S.append(int(b[i][1]))
    elif b[i][0] == "H":
        H.append(int(b[i][1]))
    elif b[i][0] == "C":
        C.append(int(b[i][1]))
    else:
        D.append(int(b[i][1]))

set_S = list(set(check)-set(S))
set_S.sort()
set_H = list(set(check)-set(H))
set_H.sort()
set_C = list(set(check)-set(C))
set_C.sort()
set_D = list(set(check)-set(D))
set_D.sort()
for i in set_S:
    print("S",i)
for i in set_H:
    print("H",i)
for i in set_C:
    print("C",i)
for i in set_D:
    print("D",i)
