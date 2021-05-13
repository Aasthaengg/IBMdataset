s = input()
k = len(s)
potential_win = 15 - k
win_cnt = s.count("o")
if win_cnt + potential_win >= 8:
    print("YES")
else:
    print("NO")