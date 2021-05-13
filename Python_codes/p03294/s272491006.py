N = int(input())
lista = list(map(int, input().split()))
ans = 0

for x in lista:
  ans+= x
  
print(ans- N)