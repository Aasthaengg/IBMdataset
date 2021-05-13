S = input()
K = int(input())
mem = 1
for i in S:
  if i != "1" or mem == K: 
    print(i)
    break
  mem += 1 
else: print("1")    