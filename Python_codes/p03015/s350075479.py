import sys
input = sys.stdin.readline

def main():
    MOD = 10**9+7
    L = input()
    K = len(L)-1
    
    dp1 = [0] * K
    dp1[0] = 1
    
    dp2 = [0] * K
    dp2[0] = 2
    
    for i in range(1, K):
        if L[i] == '0':
            dp1[i] = dp1[i-1] * 3
            dp2[i] = dp2[i-1]
        
        else:
            dp1[i] = dp1[i-1] * 3
            dp2[i] = dp2[i-1] * 2
            dp1[i] += dp2[i-1]
            
        dp1[i] %= MOD
        dp2[i] %= MOD

    print((dp1[-1]+dp2[-1])%MOD)

if __name__ == '__main__':
    main()
   