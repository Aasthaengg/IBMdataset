N = int(input())
S = [int(input()) for _ in range(N)]
T = sum(S)
L = [s for s in S if s%10!=0]
m = min(L) if len(L)>0 else T
print(T if T%10!=0 else T-m)