S = input()
t = S[0]
cnt = 0
bol = 0
for i in range(1,len(S)):
    if bol == 1:
        bol = 0
        continue
    if S[i] == t:
        t = 0
        cnt += 1
        bol = 1
    else:
        t = S[i]
print(len(S)-cnt)