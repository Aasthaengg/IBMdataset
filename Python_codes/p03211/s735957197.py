S = input()

min_number = 10**10

for i in range(len(S)-2):
    num = int(S[i]+S[i+1]+S[i+2])
    abs_i = abs(753-num)
    if abs_i < min_number:
        min_number = abs_i

print(min_number)