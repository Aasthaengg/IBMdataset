s = input()

cnt_white = 0
cnt_move = 0
for i in range(len(s)):    
    if s[i] == 'W':
        cnt_move += i - cnt_white
        cnt_white += 1
print(cnt_move)