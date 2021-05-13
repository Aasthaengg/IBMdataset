N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
ma = max(A)
n = len(bin(ma))-2
D = [0]*n
ans = 0
for i in range(n):
    zero = 0
    one = 0
    for a in A:
        if a>>i&1:
            one+=1
        else:
            zero+=1
            
    ans+=((one*zero)*2**i)%mod
    ans%=mod
print(ans)