A,B,C= list(map(int,input().split()))
if A >= C or B >= C:
   print("No")
   exit()
if 4*A*B < (C-A-B)**2:
   print("Yes")
else:
   print("No")