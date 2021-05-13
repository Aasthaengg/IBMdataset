# 初期入力
from collections import Counter
import sys
input = sys.stdin.readline  #文字列では使わない
n = int(input())
v = list(map(int, input().split()))
vo1 =v[1::2]
ve2 =v[0::2]
co1_k,co1_v = zip(*Counter(vo1).most_common())
ce2_k,ce2_v = zip(*Counter(ve2).most_common())

ans =0

if vo1 ==ve2:
    if len(ce2_k) <=2:
        ans =sum(ce2_v)
    else:
        ans =sum(ce2_v) +sum(co1_v[2:])   
elif len(co1_v) ==len(ce2_v) ==1:
    ans =0
elif co1_k[0] ==ce2_k[0]:
    if len(co1_v) ==1:
        ans =sum(ce2_v[1:])
    elif len(ce2_v) ==1:
        ans =sum(co1_v[1:])
    elif len(co1_v) ==len(ce2_v) ==2:
        ans1 =co1_v[1] +ce2_v[0]
        ans2 =co1_v[0] +ce2_v[1]
        ans =min(ans1,ans2)
    elif len(co1_v) ==2:
        ans1 =co1_v[1] +ce2_v[0] +sum(ce2_v[2:])
        ans2 =co1_v[0] +sum(ce2_v[1:])
        ans =min(ans1,ans2)
    elif len(ce2_v) ==2:
        ans1 =ce2_v[1] +co1_v[0] +sum(co1_v[2:])
        ans2 =ce2_v[0] +sum(co1_v[1:])
        ans =min(ans1,ans2)
    else:
        ans1 =sum(co1_v[1:]) +ce2_v[0] +sum(ce2_v[2:] )
        ans2 =sum(ce2_v[1:]) +co1_v[0] +sum(co1_v[2:] )
        ans =min(ans1,ans2)
else: 
    if len(co1_v) ==1:
        ans =sum(ce2_v[1:])
    elif len(ce2_v) ==1:
        ans =sum(co1_v[1:])
    else:
        ans =sum(co1_v[1:]) +sum(ce2_v[1:])  
   
print(ans)