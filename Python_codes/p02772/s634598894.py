n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
  if a[i] % 2 == 0:
    b.append(a[i])

for j in b:
  if j % 3 != 0 and j % 5 != 0:
    print('DENIED')
    exit()
    
print('APPROVED')