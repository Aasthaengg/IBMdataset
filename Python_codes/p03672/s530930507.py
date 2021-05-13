# ABC065_B
S = str(input())
N = len(S)

for i in range(1,N+1):
    T = S[0:-i]
    M = N-i
    if M % 2 == 1:
        pass
    elif T[0:(M//2)] != T[(M//2):M]:
        pass
    else:
        print(N-i)
        break
