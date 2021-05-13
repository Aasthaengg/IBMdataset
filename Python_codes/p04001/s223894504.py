S = str(input().strip())

cnt = 0
for i in range(1 << len(S)-1):
    y = None
    x = 0
    for j in range(len(S)):
        x -= 1
        if x == -len(S):
            cnt += int(S[x:y])
        elif i & (1 << j):
            cnt += int(S[x:y])
            y = x

print(cnt)