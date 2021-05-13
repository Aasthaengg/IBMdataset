n = int(input())

a=n
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    a = min(a, n//i + i -2)
print(a)