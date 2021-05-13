N = int(input())
A = list(map(int,input().split()))
maxa = max(A)
minx = min(A)
lista = [0]*(max(A)+1)
for i in range(len(A)):
  #print(A[i])
  for j in range(0,maxa+1,A[i]):
    lista[j] += 1
    #print(j)
count = 0
for i in range(len(A)):
  if lista[A[i]] == 1:
    count += 1
print(count)