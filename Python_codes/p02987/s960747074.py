S = input()

check = True
for i in range(4):
  if S.count(S[i]) != 2:
    check = False
    
print("Yes" if check else "No")