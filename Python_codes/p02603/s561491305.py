n=int(input())
a = input().split(" ")
lista = [int(n) for n in a]
kane=1000
k=0
for i in range(n-1):
  c=lista[i]
  d=lista[i+1]
  if c<d:
    b=kane//c
    kane-=b*c
    k+=b
  elif c>=d:
    kane+=k*c
    k=0
  if i==n-2:
    kane+=k*lista[n-1]
    k=0
print(kane)

