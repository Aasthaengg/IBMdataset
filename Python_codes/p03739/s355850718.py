n = int(input())
a = list(map(int, input().split()))
l = len(a)
b = []
for i in range(l):
  b.append(a[i])
  
ans = 0
Ans = 0
summary = a[0]

if(summary == 0):
  summary = 1
  ans+= 1
  Summary = -1
  Ans+= 1
else:
  b[0] = int(-a[0]/ abs(a[0]))
  Ans+= abs(a[0]- b[0])
  Summary = b[0]  
  
for i in range(1, l):
  if(summary* (summary+ a[i])>= 0):
    if(summary > 0):
      ans+= a[i]+ summary+ 1
      a[i] = -summary- 1 
      summary= -1
    else:
      ans+= -summary+ 1- a[i]
      a[i] = -summary+ 1
      summary= 1
  else:
    summary+= a[i]

for i in range(1, l):
  if(Summary* (Summary+ b[i])>= 0):
    if(Summary > 0):
      Ans+= b[i]+ Summary+ 1
      b[i] = -Summary- 1 
      Summary= -1
    else:
      Ans+= -Summary+ 1- b[i]
      b[i] = -Summary+ 1
      Summary= 1
  else:
    Summary+= b[i]
    
print(min(ans, Ans))