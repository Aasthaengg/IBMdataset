S = input()
result = [0] * len(S)

for i in range(len(S)-1, 0, -1):
    s = len(S) - i - 1
    # 右方向
    if S[s] == 'R':
        if S[s] == S[s+1]:
            result[s+2] += result[s] + 1
            result[s] = 0
        else:
            result[s] += 1

    # 左方向
    if S[i] == 'L':
        if S[i] == S[i-1]:
            result[i-2] += result[i] + 1
            result[i] = 0
        else:
            result[i] += 1

print(' '.join([str(x) for x in result]))
