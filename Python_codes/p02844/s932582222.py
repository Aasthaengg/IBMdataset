import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# 初期入力　　２０２０－０７２７　21：50
from collections import Counter
import sys
input = sys.stdin.readline  #文字列では使わない
N = int(input())
*S, =input().strip()
"""
c =Counter(S)
ans =combinations_count(N, 3) -len(c)
"""
count =0
x100=0
x10=0
x1=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if str(i) in S:
                x100 =S.index(str(i)) +1
                if str(j) in S[x100:]:
                    x10 =S[x100:].index(str(j)) +1
                    if str(k) in S[x100 +x10:]:
                        x1 =S[x100+x10:].index(str(k)) +1
                        count +=1
                        #print("aa",i,j,k,"bb",x100,x100+x10,x100+x10+x1)

print(count)