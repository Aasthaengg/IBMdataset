n, k=map(int, input().split())
import math

#まず、nがk以上だった場合、勝ちになるので、① n-k+1/n
#k-1 => 得点 >1の場合、コインを投げ、表を出し続け、k以上に出す確率
#k-1=> k/2（切り上げ）に関しては、１回表を出すから 1/2 (1乗）
#k/2(切り捨て）からk/4（切り上げ）に関しては、1/2の二乗
#print(int(math.log2(n))+1)
if n>=k:
  ans=n-k+1
  for i in range(1, k):
    ans+=(1/2)**(math.ceil(math.log2(k/i)))
else:
  ans=0
  for i in range(1, n+1):
    ans+=(1/2)**(math.ceil(math.log2(k/i)))
print(ans/n)