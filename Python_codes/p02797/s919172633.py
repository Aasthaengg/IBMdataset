N,K,S = list(map(int, input().split()))

## 1,2,3,...,N
## 1<= A <= 1e9
## sum=S, pairs=K
# K<N//2, S,MAX,S,MAX,...
# K>N//2, 

adv = 10**9 if S < 10**9 else 10**9 - 1

ans = [S] * K + [adv] * (N-K)
print(" ".join(map(str, ans)))