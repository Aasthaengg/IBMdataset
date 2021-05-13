S = list(input())
w = int(input())
o = []

for i in range(0,len(S),w):
  o.append(S[i])
  
print(''.join(o))

