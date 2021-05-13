S = input()
for i in range(97,123):
  if chr(i) in set(S):
    continue
  print(chr(i))
  exit()
print("None")