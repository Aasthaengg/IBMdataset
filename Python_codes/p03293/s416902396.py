S=input()
T=input()
a='No'
for i in range(len(T)):
  if T[i:]+T[:i]==S or T[:i]+T[i:]==S:
    a='Yes'
    break
print(a)