S = input()

for n in range(97,123):
  if chr(n) not in S:
    print(chr(n))
    exit()

print("None")