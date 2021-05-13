s = input()
s1, s2 = int(s[:2]), int(s[2:])
ans = ['NA', 'YYMM', 'MMYY', 'AMBIGUOUS']
print(ans[((1 <= s1 <= 12) << 1) + (1 <= s2 <= 12)])