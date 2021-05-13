n = int(input())
s = input()
r_cnt = s.count("R")
b_cnt = s.count("B")
if r_cnt > b_cnt:
    print("Yes")
else:
    print("No")