N = int(input())
flag =0 #yesフラグ
ext1 = N // 4
ext2 = N // 7

if ext1 == 0:
  print("No")
else:
  for i in range(ext1 +1):
    for j in range (ext2 +1):
      if i*4 + j*7 ==N:
        flag +=1
  print("Yes"if flag >0 else "No")