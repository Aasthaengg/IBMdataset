c = str(input())
alp = [chr(i) for i in range(97, 97+26)]

for i in range(26):
  if c == alp[i]:
    print(alp[i+1])
    break