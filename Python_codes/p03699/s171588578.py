N = int(input())
S = [int(input()) for i in range(N)]
S.sort()
if sum(S) % 10 != 0:
    print(sum(S))
else:
    for i in range(N):
        if S[i] % 10 != 0:
            print(sum(S)-S[i])
            exit()
    print(0)
