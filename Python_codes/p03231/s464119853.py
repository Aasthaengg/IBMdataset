import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

from math import gcd
def main():
    N,M = map(int,input().split())
    S = input()
    T = input()

    lcm = N*M//gcd(N,M)
    
    x = lcm//N
    y = lcm//M
    
    ans = lcm
    for i in range(N):
        j = x * i
        if j%y == 0:
            if S[i] != T[j//y]:
                ans = -1
                break
    
    for j in range(M):
        i = y * j
        if i%x == 0:
            if S[i//x] != T[j]:
                ans = -1
                break
    print(ans)  
if __name__ == '__main__':
    main()