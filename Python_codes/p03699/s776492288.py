N = int(input())
S = []
for i in range(N):
    S.append(int(input()))
S.sort()
if sum(S)%10!=0:
    print(sum(S))
else:
    for i in range(N):
        if S[i]%10!=0:
            print(sum(S)-S[i])
            break
        elif i==N-1:
            print(0)
            break