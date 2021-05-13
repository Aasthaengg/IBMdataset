from bisect import bisect_left, bisect_right
import random
def is_prime(q,k=50):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
 
    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

prime = []
like = [3]
for i in range(3, 10**5+1):
    if is_prime(i):
        prime.append(i)
p_set = set(prime)
for i in prime:
    if (i+1)//2 in p_set:
        like.append(i)

Q = int(input())

for _ in range(Q):
    l, r = map(int,input().split())
    print(bisect_right(like, r) - bisect_left(like, l))