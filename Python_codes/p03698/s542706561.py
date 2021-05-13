S = str(input())
a = []
for i in range(len(S)):
  if S[i] in a:
    print("no")
    quit()
  else:
    a.append(S[i])
    
    
print("yes")    