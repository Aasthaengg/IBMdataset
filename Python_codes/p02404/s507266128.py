while True:
   H, W = map(int, raw_input().split())
 
   if (H == 0 and W == 0): 
    break
   for i in range(H):
    if(i==0):
     print "#"*W
    elif(i==H-1):
     print "#"*W
    else:
     print ("#"+"."*(W-2)+"#")

   print ""