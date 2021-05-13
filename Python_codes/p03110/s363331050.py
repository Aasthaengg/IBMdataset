N = int(input())
total =0
for i in range(N):
  MM = input().split()
  if MM[-1] == 'JPY':
    total += float(MM[0])
  else:
    total += float(MM[0]) *380000
print(total)