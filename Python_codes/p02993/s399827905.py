s = input()

for i in range(0,3):
  if(s[i] == s[i+1]):
    print("Bad")
    exit()
print("Good")