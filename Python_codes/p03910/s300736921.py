N=int(input())
for i in range(1000000):
  if (i*(i+1))//2>=N:
    a=i
    break
pointer=a
while N>0:
  if N>=pointer:
    print(pointer)
    N-=pointer
    pointer-=1
  else:
    print(N)
    N=0
