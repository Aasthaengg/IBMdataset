import sys

C1 = input()
C2 = input()[::-1]


for i in range(len(C1)):
  if C1 != C2:
    print("NO")
    sys.exit()

print("YES")
    
    

