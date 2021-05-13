import sys
s=input()
for i in range(3):
  if s[i]==s[i+1]:
    print("Bad")
    sys.exit()
print("Good")