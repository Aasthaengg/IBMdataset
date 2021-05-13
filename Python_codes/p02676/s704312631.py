N = int(input())
a = input()
if len(list(a)) <=N:
  print(a)
else:
  print(a[0:N]+'...')