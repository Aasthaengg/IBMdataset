S = list(input())
T = list(input())
count = 0

for i, c in enumerate(S):
  if (c != T[i]):
    count += 1
print(count)