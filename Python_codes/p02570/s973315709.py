#A - Dont be late
D,T,S = map(int,input().split())
Time =  float(D / S )
Tf = float(T)
# 出力
if Tf >= Time :
    print('Yes')
else:
    print('No')
