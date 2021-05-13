s = input()
acgt = [0]
tmp = 0
for i in range(len(s)):
  if s[i] in ['A', 'C', 'G', 'T']:
    tmp += 1
  elif tmp > 0:
    acgt.append(tmp)
    tmp = 0

acgt.append(tmp)

print(max(acgt))