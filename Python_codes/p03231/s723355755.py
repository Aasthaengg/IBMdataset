import fractions
import bisect
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
N, M = map(int, input().split())
S = input()
T = input()
L = lcm(N,M)
S_arr = [0]*N
T_arr = [0]*M
for i in range(1,N):
    S_arr[i] = i*(L//N)
for i in range(1,M):
    T_arr[i] = i*(L//M)
if M <= N:
    for i in range(M):
        index = bisect.bisect_left(S_arr,T_arr[i])
        if S_arr[index] == T_arr[i] and S[index] != T[i]:
            print(-1)
            exit()
else:
    for i in range(N):
        index = bisect.bisect_left(T_arr,S_arr[i])
        if T_arr[index] == S_arr[i] and T[index] != S[i]:
            print(-1)
            exit()

print(L)