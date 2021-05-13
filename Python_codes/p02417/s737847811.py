n = open(0)
n = n.read()
l1 = "abcdefghijklmnopqrstuvwxyz"
l2 = [0]*26

for i in n:
   for j in range(len(l1)):
      if i == l1[j] or i == l1[j].upper():
         l2[j] += 1

for i in range(len(l1)):
   print(l1[i], ":", l2[i])
