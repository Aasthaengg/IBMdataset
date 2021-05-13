N = int(input())
Di = 0
Di1 = []
Di2 = []
nmDi = 0
if N >= 3 and N <= 100:
   for x in range(N):
      Di = input()
      Di1.append(Di[0])
      Di2.append(Di[-1])
   for x in range(N):
      if Di1[x] == Di2[x]:
         nmDi += 1
         if nmDi == 3:
            break
      elif Di1[x] != Di2[x] and nmDi > 0:
         nmDi = 0
   if nmDi >= 3:
      print("Yes")
   else:
      print("No")
else:
   print ("No")