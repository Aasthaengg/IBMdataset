N = int(input())
d = [int(x) for x in input().split()]
if(N%2==1):
  print(0)
else:
  d.sort()
  print(int(d[int(N/2)] - d[int(N/2)-1]))