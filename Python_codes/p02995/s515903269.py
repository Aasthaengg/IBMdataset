a,b,c,d = map(int,input().split())

import math
LCM=c * d //math.gcd(c, d)

tmp1=b//c + b//d - b//LCM #1~bまで調べたとき、割り切れる数の個数
tmp2=(a-1)//c + (a-1)//d - (a-1)//LCM #1~a-1まで調べたとき、割り切れる数の個数
tmp=tmp1-tmp2 #a~bまで調べたとき、割り切れる数の個数
ans=(b-a+1)-tmp

print(ans)