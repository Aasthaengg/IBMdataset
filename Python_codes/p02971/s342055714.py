n=int(input())
a=[int(input()) for _ in range(n)]
b=sorted(a)
if b[n-1]==b[n-2]:
  for i in a:
    print(b[n-1])
else:
  for i in a:
    if i==b[n-1]:
      print(b[n-2])
    else:
      print(b[n-1])