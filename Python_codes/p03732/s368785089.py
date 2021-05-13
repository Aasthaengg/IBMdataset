import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,W = MI()
w1,v = MI()
v0,v1,v2,v3 = [v],[],[],[]  # 重さが w1,w1+1,w1+2,w1+3 である荷物の価値
for i in range(N-1):
    w,v = MI()
    if w == w1:
        v0.append(v)
    elif w == w1+1:
        v1.append(v)
    elif w == w1+2:
        v2.append(v)
    else:
        v3.append(v)

v0.sort(reverse=True)
v1.sort(reverse=True)
v2.sort(reverse=True)
v3.sort(reverse=True)
N0,N1,N2,N3 = len(v0),len(v1),len(v2),len(v3)

from itertools import accumulate
v0_accumulate = [0] + list(accumulate(v0))
v1_accumulate = [0] + list(accumulate(v1))
v2_accumulate = [0] + list(accumulate(v2))
v3_accumulate = [0] + list(accumulate(v3))

ans = 0
for i in range(N0+1):  # 重さが w1 である荷物を i 個選ぶ
    for j in range(N1+1):  # 重さが w1+1 である荷物を j 個選ぶ
        for k in range(N2+1):  # 重さが w1+2 である荷物を k 個選ぶ
            for l in range(N3+1):  # 重さが w1+3 である荷物を l 個選ぶ
                if w1*i + (w1+1)*j + (w1+2)*k + (w1+3)*l <= W:
                    ans = max(ans,v0_accumulate[i]+v1_accumulate[j]+v2_accumulate[k]+v3_accumulate[l])
print(ans)
