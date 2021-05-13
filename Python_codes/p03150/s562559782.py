import re
S=input()
if re.fullmatch(r"[a-z]*keyence",S)==None and re.fullmatch(r"k[a-z]*eyence",S)==None and re.fullmatch(r"ke[a-z]*yence",S)==None and re.fullmatch(r"key[a-z]*ence",S)==None and re.fullmatch(r"keye[a-z]*nce",S)==None and re.fullmatch(r"keyen[a-z]*ce",S)==None and re.fullmatch(r"keyenc[a-z]*e",S)==None and re.fullmatch(r"keyence[a-z]*",S)==None:
  print("NO")
else:
  print("YES")