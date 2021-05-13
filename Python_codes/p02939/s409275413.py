S = input()

l = [0]*len(S)

l[0] = 1

if S[0] != S[1]:
  l[1] = 2
else:
  l[1] = 1

for i in range(2,len(S),1):
  if S[i] != S[i-1]:
    l[i] = l[i-1]+1
  else:
    l[i] = l[i-3]+2
print(l[len(l)-1])