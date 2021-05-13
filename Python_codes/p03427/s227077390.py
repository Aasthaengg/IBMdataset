X = list(map(int,input()))
sn = []
for i in range(len(X)):
  sn.append(sum(X[0:i+1]))
ssn = []
for i in range(len(X)):
  if (sn[i] != 0):
    ssn.append(sn[i]-1 + 9*(len(X)-1-i))
ssn.append(sum(X))
print(max(ssn))