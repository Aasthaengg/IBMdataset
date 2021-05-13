# 月のフォーマットによる場合分け。
s = list(input())
# 前二桁
s1 = int("".join(s[:2]))
# 後二桁
s2 = int("".join(s[2:]))

# 前二桁と後二桁に月の可能性がある。
if 1 <= s1 <= 12 and 1 <= s2 <= 12:
    print('AMBIGUOUS')
elif 1 <= s1 <= 12:
    print('MMYY')
elif 1 <= s2 <= 12:
    print('YYMM')
else:
    print('NA')
