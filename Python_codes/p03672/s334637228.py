S = input()

front_str = ''
back_str = ''
result = 0
for i in range(2, len(S)-1, 2):
    front_str = S[:int(i/2)]
    back_str = S[int(i/2):i]
    tmp_len = 0
    if front_str == back_str:
        tmp_len = i
        result = max(result, tmp_len)

print(result)