import string
C = input()
R = string.ascii_lowercase

for i, r in enumerate(R):
  if r == C:
    print(R[i + 1])