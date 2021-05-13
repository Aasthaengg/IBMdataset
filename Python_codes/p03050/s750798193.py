N = int(input())

i = 1
rlt = 0
while N > i**2 + i:
  if (N-i)%i == 0:
    rlt += (N-i)//i
  i += 1
    
print(rlt)