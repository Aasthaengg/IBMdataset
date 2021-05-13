import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7


N = int(readline())
A = list(map(int,readline().split()))
B = list(map(int,readline().split()))
Ka = sum(B)-sum(A)
Kb = Ka
for a,b in zip(A,B):
    if a > b:
        Kb -= a-b
    else:
        if (b-a)%2:
            Ka -= (b-a+1)//2
            Kb -= 1
        else:
            Ka -= (b-a)//2
print('Yes' if Ka >= 0 and Kb >= 0 else 'No')


