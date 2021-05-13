n = int(input())
S = sorted([int(input()) for _ in range(n)])

if sum(S)%10!=0:
    print(sum(S))
    exit()
for i in range(n):
    if S[i]%10==0:
        continue
    print(sum(S)-S[i])
    exit()
print(0)


