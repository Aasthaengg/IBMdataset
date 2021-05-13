x=int(input())
for i in range(int(x**.3+1)):
  for j in range(-int((x**.3+1)),int(x**.3+1)):
    if i**5-j**5==x:
      print(i,j)
      exit()