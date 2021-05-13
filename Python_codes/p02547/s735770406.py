N = int(input())

count = 0

for i in range(N):
    k, t = map(int, input().split())
      
    if not k == t:
        count *= 0
    if k == t:
       count += 1 
    if count == 3:
      print ( "Yes" )
     
      break
        
if count == 3:
        print ("")
else:
  print ("No")

