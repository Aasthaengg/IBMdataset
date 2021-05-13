n = int(input())
mn = float("inf")
for i in range(1,n):
  if sum(map(int,str(i))) + sum(map(int,str(n-i))) < mn:
    mn = sum(map(int,str(i))) + sum(map(int,str(n-i)))
print(mn)