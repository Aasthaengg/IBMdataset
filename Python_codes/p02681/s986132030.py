s = str(input())
t = str(input())

if all(s[i]==t[i] for i in range(len(s))):
  if len(s) + 1 == len(t):
    print("Yes")
    exit()
    
    
print("No")