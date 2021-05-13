# 初期入力
import sys
input = sys.stdin.readline
N,M = (int(i) for i in input().split())
A=[0]*N
B=[0]*N
for i in range(N):
    a,b = (int(i) for i in input().split())
    A[i] =(a,b)

#　1本が安い順にソート、安店から順番に買う
A.sort()
num_sum =0
price_sum =0
for i in range(N):
    price,num =A[i]
    if num_sum < M -num:
        num_sum  +=num
        price_sum += price *num
    elif num_sum == M -num:
        price_sum +=price *num
        break
    else:
        price_sum +=price*(M -num_sum)
        break
print(price_sum)