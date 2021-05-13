a,b,c,k = map(int,input().split())

if k<=a:
  print(k)
elif a< k <= a+b:
  print(a)
elif a+b < k <= a+b+c:
  print(a-(k-b-a))