N = int(input())
a,b = map(str,input().split())
a = list(a)
b = list(b)
name = ''
for i in range(N*2):
  if i%2==0:
    name+=a[int(i/2)]
  else:
    name+=b[int(i/2)]
print(name)