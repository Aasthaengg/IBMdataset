N = int(input())
S = [0]*N
for i in range(N):
    a = int(input())
    a -= 1
    if a == 0:
        S[0] = 1
    else:
        if S[a-1] == 0:
            S[a] = 1
        else:
            S[a] = S[a-1] + 1
print(N-max(S))