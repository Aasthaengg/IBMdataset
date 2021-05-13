S = input()
K = int(input())

lst = []
b = ""
tmp = 0
rlt = 0
for s in S:
  if s == b:
    tmp += 1
  else:
    lst.append(tmp)
    tmp = 1
  b = s
    
lst.append(tmp)

if len(lst) == 2:
  rlt = (lst[1]*K)//2

elif S[0] == S[-1]:
  rlt = ((lst[1]+lst[-1])//2)*(K-1) + lst[1]//2 + lst[-1]//2
  for t in lst[2:-1]:
    rlt += (t//2)*K
else:
  for t in lst[1:]:
    rlt += (t//2)*K
    
print(rlt)
