s = input()

for i in range(len(s)):
  if s.count(s[i]) > 1:
    print("no")
    exit()
    
print("yes")