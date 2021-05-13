while True:
   H,W=map(int,raw_input().split())
   if H==W==0:
       break
   elif H!=0 or W!=0:
     for i in range(0,H):
       if i%2 == 0:
         if W%2 == 1:
           print '#.'*(W/2)+'#'
         elif W%2 == 0:
           print '#.'*(W/2)
       else:
         if W%2 == 1:
           print '.#'*(W/2)+'.'
         elif W%2 == 0:
           print '.#'*(W/2)
     print ''