s = input()

s_a = int(s[:2])
s_b = int(s[2:])

if s_a >= 1 and s_a <=12 and s_b >= 1 and s_b <=12:
  ans = "AMBIGUOUS"
elif (s_a > 12 or s_a == 0) and s_b >= 1 and s_b <=12:
  ans = "YYMM"
elif (s_b > 12 or s_b == 0) and s_a >= 1 and s_a <=12:
  ans = "MMYY"
else:
  ans = "NA"

print(ans)