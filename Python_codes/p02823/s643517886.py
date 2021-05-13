n, a, b = map(int, input().split())
if (a+b)%2:
  if a-1 <= n-b:
    print(a+(b-a-1)//2)
  else:
    print(n-b+1+(n-(a+n-b+1))//2)
else:
  print((b-a)//2)