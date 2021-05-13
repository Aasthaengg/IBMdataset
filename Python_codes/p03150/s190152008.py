A=input()
if A=="keyence" or A[:7]=="keyence" or A[-7:]=="keyence":
   print("YES")
   exit()
for i in range(6):
   if A[:i+1]+A[-6+i:]=="keyence":
      print("YES")
      exit()
print("NO")