S = list(input())
value = [0] * (len(S) + 1)
  
for i in range(len(S)):
  if S[i] == '<':
    if value[i] == 0:
      value[i+1] = 1
    else:
      value[i+1] = value[i] + 1

for i in reversed(range(len(S))):
  if S[i] == '>':
    if value[i+1] == 0 and value[i] == 0:
      value[i] = 1
    elif value[i] <= value[i+1]:
      value[i] = value[i+1] + 1
print(sum(value))
