S = input()
cnt_0 = S.count("0")
cnt_1 = len(S) - cnt_0
print(min(cnt_0, cnt_1) * 2)
