S=input()
N=len(S)
answer=0
saidai=N-1
for n in range(N):
    if S[n]=='B':
        answer+=saidai-n
        saidai-=1

print(answer)
