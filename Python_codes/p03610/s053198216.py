s = input()
t = ""

for i in range(1,len(s)+1):
  if i % 2 == 1:
    t += s[i-1]
    
print(t)