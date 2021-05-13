S = input()
if S.replace("A", "") != "KIHBR":
  print("NO")
elif "AA" in S or "KA" in S or "IA" in S:
  print("NO")
else:
  print("YES")
