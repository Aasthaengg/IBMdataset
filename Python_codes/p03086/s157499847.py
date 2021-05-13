S = input()
maximum = 0
cnt = 0
for i in range(len(S)):
    if S[i] in ['A','T','C','G']:
        cnt += 1
        maximum = max(maximum,cnt)
    else:
        cnt = 0
print(maximum)