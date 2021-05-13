S = input()
flag = True
count = 0
if not S[0] == "A":
  flag = False
for i in range(2,len(S)-1):
  if S[i] == "C":
    count += 1
  else:
    if not S[i].islower():
      flag = False
if not S[1].islower():
  flag = False
if not S[len(S)-1].islower():
  flag = False
if not count == 1:
  flag = False
if flag:
  print("AC")
else:
  print("WA")