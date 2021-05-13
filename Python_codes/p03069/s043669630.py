n = int(input())
s = input()

black_right, min_val = 0, 2000001
white_left = s.count('.')
ans = [white_left+black_right]

for moji in s:
    if moji == '.':
        white_left -=1
    else:
        black_right += 1
    ans.append(white_left+black_right)
    #min_val = min(min_val, white_left+black_right)

print(min(ans))