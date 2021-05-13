N = int(input())
S = input()

def pcnt(x):
    return str(bin(x)).count("1")

dpl = 5*10**5
dp = [0] * dpl
for i in range(1, dpl):
    dp[i] = dp[i % pcnt(i)]+1

c = S.count("1")
a = int(S, 2) % (c+1)
 
def f():
    if c == 1:
        for i in range(N):
            if S[i] == "0":
                print(dp[(a + pow(2, N-i-1, c+1)) % (c+1)] + 1)
            else:
                print(0)
        return
    
    b = int(S, 2) % (c-1)
    for i in range(N):
        if S[i] == "0":
            print(dp[(a+pow(2, N-i-1, c+1))%(c+1)]+1)
        else:
            print(dp[(b-pow(2, N-i-1, c-1))%(c-1)]+1)

f()