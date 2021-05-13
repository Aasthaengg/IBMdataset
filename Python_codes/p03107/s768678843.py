s = input()

cnt0 = s.count("0")
cnt1 = s.count("1")

print(min(cnt0, cnt1) * 2)