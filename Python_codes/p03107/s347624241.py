S = input()
total = 0
count_0 = S.count("0")
count_1 = S.count("1")
ans = min(count_0, count_1) * 2
print(ans)