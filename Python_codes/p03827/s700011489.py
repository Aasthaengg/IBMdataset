firstline = int(input())
sec = input()
maxN = 0
init = 0

for i in sec:
  if i == "I":
    init += 1
  else:
    init -= 1
  if init > maxN:
    maxN = init
    
print(maxN)