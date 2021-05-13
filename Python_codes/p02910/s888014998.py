S = input()
a = "Yes"

if "L" in S[0::2] or "R" in S[1::2]:
  a = "No"

print(a)