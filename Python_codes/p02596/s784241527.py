#C
# 7,77,777･･･=7*(1,11,111･･･)
# 7*(10^i)=7*(10^i-1)/10-1 = 7*(10^i-1)/9 がkで割れる
# 10^iを(9k,7の倍数だったら9k/7)で割ってあまりが１だったら良い
import sys
k=int(input())
if k%7==0:
    k//=7
k*=9
a=10%k
for i in range(k):
    a=a%k
    if a==1:
        print(i+1)
        sys.exit()
    a*=10
print(-1)
