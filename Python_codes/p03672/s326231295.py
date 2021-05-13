S = input().strip()
cnt = 0
for i in range(len(S)-3,-1,-2):
    if S[:(i+1)//2]==S[(i+1)//2:i+1]:
        cnt = (i+1)
        break
print(cnt)