N = int(input())
lista = list(map(int, input().split()))
a = 0
b = sum(lista)
ans = abs(lista[0]- (b- lista[0]))

for i in range(N- 1):
  a+= lista[i]
  b-= lista[i]
  if(abs(a- b)< ans):
    ans = abs(a- b)
    
print(ans)