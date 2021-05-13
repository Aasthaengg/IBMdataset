s=list(input())
import sys
for i in range(1,4):
  if s[i]==s[i-1]:
    print("Bad")
    sys.exit()
    
print("Good")
  
