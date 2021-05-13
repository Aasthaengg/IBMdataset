s = input()
a_cnt = s.count("a")
b_cnt = s.count("b")
c_cnt = s.count("c")
cnt = len(s)
if max(a_cnt, b_cnt, c_cnt) - min(a_cnt, b_cnt, c_cnt) <= 1:
    print("YES")
else:
    print("NO")