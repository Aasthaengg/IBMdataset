# 初期入力
from collections import defaultdict
import sys
#input = sys.stdin.readline  #文字列では使わない
S =list(input())
T =list(input())

#
S_conversion =defaultdict(str)
T_conversion =defaultdict(str)
ans ="Yes"
if S ==T:
    ans ="Yes"
else:
    for i in range(len(S)):
        if S_conversion[S[i]] =="" and T_conversion[T[i]] =="":
            S_conversion[S[i]] =T[i] 
            T_conversion[T[i]] =S[i]
        elif S_conversion[S[i]] ==T[i]:
            continue
        elif T_conversion[T[i]] ==S[i]:
            continue
        else:
            ans ="No"
            #print(i)
            break
print(ans)