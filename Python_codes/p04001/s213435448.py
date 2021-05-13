S = input()
S_damy = S
sum_S = 0
plus = 2**(len(S)-1)
for i in range(plus):
    for j in range(len(S)-1):
        if i >> j & 0b1:
            sum_S += int(S_damy[len(S)-1-j:])
            if S_damy:
                S_damy = S_damy[:len(S)-1-j]

        if j == len(S)-2 and S_damy:
            sum_S += int(S_damy)
    S_damy = S
if len(S) == 1:
    print(S)
else:
    print(sum_S)