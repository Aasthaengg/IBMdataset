N = int(input())

#長さN, Mまでの数字を用いてtmpから始まる短調増加数字列（1123,1234など）を全て出力
from collections import deque
from collections import defaultdict
d = defaultdict(int)
n,m=3,100
y = [[x] for x in range(1,50+1)]
tmp=deque(y)
out=0
while tmp:
    T=tmp.pop()
    if len(T) < n:
        for i in range(int(T[-1]),m+1):
            tmp.append(T+[i]) 
    else:
        ans = int((sum(T))**2-(T[0]*T[1]+T[1]*T[2]+T[2]*T[0]))
        if ans <= 10000:
            if T[0] == T[1] and T[1] == T[2]:
                plus = 1
            elif T[0] == T[1] or T[1] == T[2]:
                plus = 3
            else:
                plus = 6
            d[ans] += plus
            
for i in range(N):
    print(d[i+1])