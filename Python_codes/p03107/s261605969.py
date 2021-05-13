S = input()
cnt0 = S.count("0")
cnt1 = S.count("1")
ans = min(cnt0, cnt1) * 2
print(ans)
