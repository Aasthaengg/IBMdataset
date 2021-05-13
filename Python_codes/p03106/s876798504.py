A, B, K = list(map(lambda x: int(x), input().split(" ")))
cd = []
for i in range(min([A,B])):
  if A % (i + 1) == 0 and B % (i + 1) == 0:
    cd.append(i+1)
 
print(cd[-K])