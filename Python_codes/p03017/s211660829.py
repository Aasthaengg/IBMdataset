import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N,A,B,C,D = map(int,readline().split())
S = readline().rstrip()

if C < D:#抜かさなくて良い
    if "##" not in S[A-1:D]:
        print("Yes")
    else:
        print("No")
else:#抜かす必要がある
    if "..." in S[B-2:D+1] and "##" not in S[A-1:C]:
        print("Yes")
    else:
        print("No")

