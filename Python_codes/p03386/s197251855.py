4,5,6,7,8,9,10
a, b , k = map(int, input().split())
if k > (b-a)//2:
  for i in range(a, b+1):
    print(i)
else:
  for i in range(a, a+k):
    print(i)
  for j in range(b-k+1,b+1):
    print(j)