S = input ()
T = input ()
X = 'No'
for i in range (len(S)):
  if T == S[i:]+S[:i]:
    X = 'Yes'
    break
print (X)