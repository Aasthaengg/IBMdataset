A=input()
l=set(chr(ord('a') + i) for i in range(26))
l2=list(l-set(A))
l2.sort()
if len(A)!=26:
   print(A+l2[0])
else:
   for i in reversed(range(25)):
      for j in reversed(range(i+1,26)):
         if A[i] < A[j]:
            print(A[:i]+A[j])
            exit()
   else:
      print(-1)