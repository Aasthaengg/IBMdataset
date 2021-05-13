s = input()
cnt_1 = s.count("1")
cnt_0 = s.count("0")

print(2 * min(cnt_1, cnt_0))