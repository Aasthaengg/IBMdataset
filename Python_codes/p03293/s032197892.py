S = input()
T = input()
N = len(S)
for i in range(N):
    S_i = S[(N-i-1):] + S[:(N-i-1)]
    if S_i == T:
        print('Yes')
        exit()

print('No')