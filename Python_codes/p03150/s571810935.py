S = input()
original_str = "keyence"

for i in range(len(S)):
  for j in range(i,len(S)):
    s = "".join([S[:i],S[j:]])
    if s == original_str:
      print("YES")
      exit()
    
print("NO")