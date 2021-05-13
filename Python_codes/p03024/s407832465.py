s = input()
ans = "NO"
if s.count("x") >= 8: ans = "NO"
elif 8 - s.count("o") <= 15 - len(s): ans = "YES"
print(ans)