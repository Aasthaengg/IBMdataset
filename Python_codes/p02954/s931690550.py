S = input()

length = [0] * len(S)
child = [0] * len(S)

index = 0
count = 0
while index < len(S):
  while index < len(S) and S[index] == "R":
    index += 1
  count = 1
  while index < len(S) and S[index] == "L":
    length[index] = -count
    index += 1
    count += 1

index = 0
count = 0
while index < len(S):
  while index < len(S) and S[len(S) - index - 1] == "L":
    index += 1
  count = 1
  while index < len(S) and S[len(S) - index - 1] == "R":
    length[len(S) - index - 1] = count
    index += 1
    count += 1

for i in range(len(S)):
  if length[i] > 0:
    l = length[i] - 1
    child[i + l + l % 2] += 1
  else:
    l = abs(length[i]) - 1
    child[i - l - l % 2] += 1

for i in range(len(S)):
  print(child[i], end="")
  if i != len(S) - 1:
    print(" ", end="")
print()
