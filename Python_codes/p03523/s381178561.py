s=input()
p=""
for c in s:
  if c!="A":
    p+=c
print(("NO","YES")[p=="KIHBR" and "AA" not in s and "KA" not in s and "IA" not in s])
