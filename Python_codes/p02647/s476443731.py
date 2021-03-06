# imos法
# 長さNの1次元配列において、「ある連続する区間に、ある数vを足す」という操作をK回繰り返した結果を高速で求める
# 
    
# 初期入力
    
import sys
input = sys.stdin.readline
N,K = (int(i) for i in input().split())
A = list(map(int, input().split()))
    
    
l =0
r =N
cumulative_sum =[0]*N
#操作数が電球の数より多いとき
if N <=K:
    A=[N]*N
# imos法
else:
    for j in range(K):
        B =[0]*(N+1)
        for i in range(N):
            index =A[i]
            if i-index <0:
                l=0
            else:
                l =i -index
            if i +index +1 >=N:
                r =N 
            else:
                r =i +index +1
            B[l] +=1 
            B[r] -=1
        #累積和(imos法) 
        from itertools import accumulate
        del B[-1]
        A =list(accumulate(B))
        if sum(A) ==N*N:
            print(*A)
            sys.exit(0)
    
print(*A)
