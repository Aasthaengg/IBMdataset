# -*- coding: utf-8 -*-
 
I = ["dream", "dreamer", "erase", "eraser"]
I2 = input()
 
if I2.replace(I[1], "").replace(I[0], "").replace(I[3], "").replace(I[2], "").strip() == "":
  print("YES")
elif I2.replace(I[0], "").replace(I[2], "").replace(I[1], "").replace(I[3], "").strip() == "":
  print("YES")
elif I2.replace(I[2], "").replace(I[0], "").replace(I[3], "").replace(I[1], "").strip() == "":
  print("YES")
elif I2.replace(I[3], "").replace(I[2], "").replace(I[1], "").replace(I[0], "").strip() == "":
  print("YES")
else:
  print("NO")