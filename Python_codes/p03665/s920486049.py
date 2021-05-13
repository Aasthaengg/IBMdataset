import sys
sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15
from bisect import bisect_left,bisect_right

def main():  
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    cnt1 = sum(a%2 == 1 for a in A)
    cnt0 = N - cnt1
    factorial = [1,1]
    for i in range(2,N + 1):
        factorial.append(factorial[-1]*i)
    
    nck = lambda n,k:factorial[n]//factorial[n - k]//factorial[k]

    ans = 0
    if P == 0:
        for i in range(0,cnt1 + 1,2):
            ans += nck(cnt1,i)
        ans *= pow(2,cnt0)
    else:
        for i in range(1,cnt1 + 1,2):
            ans += nck(cnt1,i)
        ans *= pow(2,cnt0)
    print(ans)
if __name__ == '__main__':
    main()