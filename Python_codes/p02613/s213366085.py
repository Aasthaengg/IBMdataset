N = int(input())
S = list()
for i in range(N):
    S.append(input())

c0 = 0
c1 = 0
c2 = 0
c3 = 0

for i in S:
  if i == "AC":
    c0 += 1
    
  if i == "WA":
    c1 += 1

  if i == "TLE":
    c2 += 1
    
  if i == "RE":
    c3 += 1
  
  
print("AC x " + str(c0))
print("WA x " + str(c1))
print("TLE x " + str(c2))
print("RE x " + str(c3))
