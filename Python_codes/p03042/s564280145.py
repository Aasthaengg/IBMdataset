s = input()

s_a = int(s[:2])
s_b = int(s[2:])

if 1 <= s_a <=12 and 1 <= s_b <=12:
  ans = "AMBIGUOUS"
elif not(1 <= s_a <=12) and 1 <= s_b <=12:
  ans = "YYMM"
elif 1 <= s_a <=12 and not(1 <= s_b <=12):
  ans = "MMYY"
else:
  ans = "NA"

print(ans)