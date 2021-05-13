import fractions
N, M = map(int, input().split())
S = input()
T = input()

def lcm(x, y):
    return (x*y)//(fractions.gcd(x, y))

L = lcm(N, M)
num = lcm(L//N, L//M)

n = (N-1)*(L//N)+1
m = (M-1)*(L//M)+1

if(max(n, m) < num):
    if(S[0] == T[0]):
        print(L)
    else:
        print(-1)
else:
    if(N > M):
        tmp = M//(L//N)
    else:
        tmp = N//(L//M)
    for i in range(tmp):
        if(S[i*L//M] != T[i*L//N]):
            print(-1)
            break
    else:
        print(L)