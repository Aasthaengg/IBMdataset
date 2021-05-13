import numpy as np
str = input()
char_list = list(str)
lest_win=8-char_list.count("o")
lest_day=15-len(char_list)
if lest_win > lest_day:
    print("NO")
else:
    print("YES")