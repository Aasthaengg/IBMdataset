N = int(input())
d = sorted(list(map(int, input().split())))
if d[int(N/2)-1] == d[int(N/2)]:
  print(0)
else:
  
  print(d[int(N/2)]-d[int(N/2)-1])