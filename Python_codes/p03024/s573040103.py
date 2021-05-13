s= input()
win_num = s.count("o")
rest_game = 15-len(s)

if win_num + rest_game>=8:
    print("YES")
else:
    print('NO')