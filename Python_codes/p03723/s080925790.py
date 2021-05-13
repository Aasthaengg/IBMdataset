A,B,C = map(int,input().split())
tmpA = 0
tmpB = 0
tmpC = 0
count = 1
if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
  print(0)
  exit()
if A == B and A == C and B == C:
  print(-1)
  exit()

while True:
  tmpA = (B + C) / 2
  tmpB = (A + C) / 2
  tmpC = (A + B) / 2
  if tmpA % 2 == 1 or tmpB % 2 == 1 or tmpC % 2 == 1:
    break
  else:
    A = tmpA
    B = tmpB
    C = tmpC
    count += 1
print(count)