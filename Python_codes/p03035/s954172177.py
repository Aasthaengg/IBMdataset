n,k=tuple(map(int,input().split()))
if n >= 13:
  print(k)
elif 6 <= n <= 12:
  print(k//2)
elif n <= 5:
  print(0)
