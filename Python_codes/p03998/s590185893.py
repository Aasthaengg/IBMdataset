Sa = str(input())
Sb = str(input())
Sc = str(input())
S = [[ord(i)-97 for i in Sa], [ord(i)-97 for i in Sb], [ord(i)-97 for i in Sc]]

flag = True
who = 0
while flag:
  if S[who] != []:
    tmp = S[who][0]
    S[who].pop(0)
    who = tmp
  else:
    if who == 0:
      ans = 'A'
    elif who == 1:
      ans = 'B'
    else:
      ans = 'C'
    break
print(ans)