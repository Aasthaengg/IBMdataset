N = int(input())
S = input()

white_sum = 0
for i in range(N):
    if S[i] == '#':
        continue
    else:
        white_sum += 1

left_black = 0
right_white = white_sum
min_sum = white_sum
for i in range(N):
    if S[i] == '#':
        left_black += 1
    else:
        right_white -= 1

    min_sum = min(min_sum, left_black + right_white)
print(min_sum)
