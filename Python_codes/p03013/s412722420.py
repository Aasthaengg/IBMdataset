N, M = map(int, input().split())
if N == 1:
    print(1)
    quit()
S = [-1] * (N + 1)
S[0] = 1
for i in range(M):
    S[int(input())] = 0
if S[1] != 0:
    S[1] = 1
for i in range(2, N + 1):
    if S[i] == 0:
        continue
    else:
        S[i] = (S[i - 1] + S[i - 2]) % 1000000007
        if S[i] == 0:
            print(0)
            quit()
print(S[N])