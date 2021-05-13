import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N,A,B,C,D = map(int,readline().split())
S = readline().rstrip()

if C < D:
    if S[B-1:D].find('##') == -1 and S[A-1:C].find('##') == -1:
        print('Yes')
    else:
        print('No')
else:
    if S[B-1:D].find('##') == -1 and S[A-1:C].find('##') == -1 and S[B-2:D+1].find('...') != -1:
        print('Yes')
    else:
        print('No')
