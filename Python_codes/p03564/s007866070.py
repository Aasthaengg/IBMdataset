n=int(input())
k=int(input())
a=1
for n in range(n):
  a+=min(a,k)
print(a)