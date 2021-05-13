n=int(input())
l=list(map(int, input().split()))
if n%2==0:
  for i in range(n-1, 0, -2):
    print(str(l[i]), end=' ')
  for i in range(0, n, 2):
    print(str(l[i]), end=' ')
else:
  for i in range(n-1, -1, -2):
    print(str(l[i]), end=' ')
  for i in range(1, n, 2):
    print(str(l[i]), end=' ')