a = raw_input().split()

def change(a):
 for i in range(0,3):
  for j in range(0,3):
   if a[i] < a[j]:
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
 print str(a[0])+" "+str(a[1])+" "+str(a[2])

change(a)