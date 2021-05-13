import sys
 
BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001
 
 
S = str(input())
P = str(input())
 
is_ok = False
 
for i in range(len(S)):
    FLG = True
    for k in range(len(P)):
        if S[(i+k)%(len(S))] != P[k]:
            FLG = False
            break
 
    if FLG == True:
        is_ok = True
        break
 
if is_ok == True:
    print("Yes")
else:
    print("No")
