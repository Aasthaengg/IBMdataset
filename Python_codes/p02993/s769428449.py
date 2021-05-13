s=input()
for i,j in zip(s[0:],s[1:]):
  if i==j:
    print("Bad")
    exit()
print("Good")