n = int(input())
s = str(input())
White_rui = [0]
Black_rui = [0]

white = 0
black = 0
for i in range(n):
    if s[i] == '.':
        white += 1
    else:
        black += 1
    White_rui.append(white)
    Black_rui.append(black)

ans = 10**6
for i in range(n):
    white_to_black = White_rui[-1] - White_rui[i+1]
    black_to_white = Black_rui[i] - Black_rui[0]
    ans = min(ans, white_to_black+black_to_white)

print(ans)