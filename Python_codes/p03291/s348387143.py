import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


def main():
    S=["D"] + list(input())
    N=len(S)
    MOD=10**9+7

    A = [0] * (N+1)
    C = [0] * (N+1)
    Q = [0] * (N+1)

    for i in range(1,N+1):
        s = S[i-1]
        A[i] = A[i-1]
        C[i] = C[i-1]
        Q[i] = Q[i-1]
        if s == "A":
            A[i] += 1
        elif s == "C":
            C[i] += 1
        elif s == "?":
            Q[i] += 1
    
    # print(A,C,Q)
    ans = 0
    for i in range(1,N+1):
        s = S[i-1]
        if s == "?" or s == "B":
            l_A = A[i-1]
            l_Q = Q[i-1]
            r_Q = Q[-1] - Q[i]
            r_C = C[-1] - C[i]

    
            left = pow(2,l_Q,MOD) * l_A % MOD # 一個も使わないとき
            if l_Q > 0:
                left += l_Q * pow((1+pow(2,MOD-2,MOD)), l_Q-1,MOD) * pow(2,l_Q-1,MOD) % MOD # 1個以上使うとき
                left %= MOD
                left += l_A * (pow(3,l_Q,MOD)-pow(2,l_Q,MOD)) % MOD 


            right = pow(2,r_Q,MOD) * r_C % MOD # 一個も使わないとき
            if r_Q > 0:
                right += r_Q * pow((1+pow(2,MOD-2,MOD)), r_Q-1,MOD) * pow(2,r_Q-1,MOD) % MOD # 1個以上使うとき
                right %= MOD
                right += r_C * (pow(3,r_Q,MOD)-pow(2,r_Q,MOD)) % MOD 

            ans += left * right % MOD
            ans %= MOD


            
    ans %= MOD
    print(ans)






if __name__ == "__main__":
    main()