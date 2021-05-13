s = input()
o = s.count('o')

ans = "YES" if o + (15 - len(s)) > 7 else "NO"
print(ans)