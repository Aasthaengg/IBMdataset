s=input()

alp="abcdefghijklmnopqrstuvwxyz"

ans="None"
for i in alp:
  if i not in s:
    ans=i
    break
    
print(ans)