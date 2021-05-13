import sys
M=input()
 
for i in range(10):
  if(M.find(str(i)*3)!=-1):
    print("Yes")
    sys.exit()
print("No")
