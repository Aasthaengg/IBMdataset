def div2(N):
  if(N % 2 != 0):
    return 0
  else:
    i = 0
    while N % 2 == 0:
      N/= 2
      i+= 1
    return i
  
N = int(input())
lista = list(map(int, input().split()))

ans = 0
for x in lista:
  ans+= div2(x)
  
print(ans)  