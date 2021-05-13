N=int(input())
l=[int(input()) for i in range(N)]
if all(i%2==0 for i in l):
   print("second")
else:
   print("first")