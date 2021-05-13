N = input()
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
C = list(map(int,input().split(" ")))

buffer = 0
sati = 0

for i in A:
  sati += B[i - 1]
  if buffer == 0:
    buffer = i
    continue
  elif buffer == i - 1:
    sati += C[buffer -1]
  buffer = i
print(sati)