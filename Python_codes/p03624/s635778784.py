L=list(input())
L=list(set(L))
L=sorted(L)
R=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(min(26,len(L))):
  if L[i]!=R[i]:
    print(R[i])
    exit()
if len(L)<26:
  print(R[len(L)])
  exit()
print("None")