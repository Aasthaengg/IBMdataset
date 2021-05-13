length = int(input())
list_p = list(map(int,input().split()))
#list_p.sort()
count = 0
for i in range(length):
  if list_p[i] != (i+1):
    count += 1
 
if count <= 2 :
  print ("YES")
else :
  print ("NO")