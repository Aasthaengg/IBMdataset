s = input()
t = input()
ans = "No"
for i in range(len(t)):
  if s == t:
    ans = "Yes"
    break
  else:
    tmp = t[0]
    t = t[1:] + t[0]
    
print(ans)