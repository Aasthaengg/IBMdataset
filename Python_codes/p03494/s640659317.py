N = input()
A = list(map(int,input().split()))
c = 0
d = -1
while c>d:
  d+=1
  for i in A:
    if i%2 == 0:
      continue
    else :
      print(c)
      break
  else :
    A=list(map(lambda x :x/2,A))
    c += 1

