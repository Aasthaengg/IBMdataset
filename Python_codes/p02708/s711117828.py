import itertools
n, k  = map(int,input().split())
ans =0
for i in range(k,n+2):  #i 個選ぶ
    min = i*(i-1)//2
    max = i*(2*n-i+1)//2
    ans += max-min+1
    ans %=(10**9+7)
print(int(ans))