N,M=map(int,input().split())
S=input() # 元の双六
T=S[::-1] # 逆順の双六
l=[]

f=True
i=0 # ゴールから辿る
while i<N:
    t=T[i+1:i+M+1][::-1] # 逆順の双六で今いるマスの1~Mマス先（元の双六ではM~1マス前）
    # print(t) #DB
    if '0' not in t: # 通常のマスがない場合
        f=False
        break
    else: # 通常のマスがある場合
        x=min(M-t.index('0'),len(t)) # 元の双六で，最も手前にある通常のマスまでのマス数
        # print(x) #DB
        l.append(x)
        i+=x
# print(l) #DB

if not f:
    print('-1')
else:
    print(*l[::-1],sep=' ')