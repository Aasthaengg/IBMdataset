N, K = map(int,input().split())
 
count = 0
 
# N = n*b + r
for b in range(1,N+1):
    n = N // b
    r = N % b
    count += n*max(0,b-K) + max(0,r-K+1)
 
# a=0の場合を引く
if K==0:
    count -= N
 
print(count)