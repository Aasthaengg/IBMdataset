S = input()
res=0

def doubleCheck(moji):
  n = len(moji)//2
  if len(moji) % 2 ==1:
    return False
  else:
    if moji[0:n] == moji[n:len(moji)]:
      return True
    else:
      return False

for i in range(len(S)):
  S = S[0:len(S)-1]
  if doubleCheck(S):
    res = len(S)
    break
print(res)