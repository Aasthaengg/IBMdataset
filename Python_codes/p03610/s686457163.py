import math
S=str(input())
s = ""
for i in range(math.ceil(len(S)/2)):
  s = s + S[2*i]
print(s)