S = list(input())
ANS = [0]*len(S)
count = 0
for i in range(len(S)):
    if S[i] == 'L':
        count = 0
    elif S[i] == 'R':
        count += 1
        if i != len(S)-1 and S[i+1] == 'L':
            ANS[i] += count//2+count%2
            ANS[i+1] += count//2
        elif i == len(S)-1:
            ANS[i] += count
count = 0
for i in range(len(S)-1,-1,-1):
    if S[i] == 'R':
        count = 0
    elif S[i] == 'L':
        count += 1
        if i != 0 and S[i-1] == 'R':
            ANS[i] += count//2+count%2
            ANS[i-1] += count//2
        elif i == 0:
            ANS[i] += count
print(*ANS)