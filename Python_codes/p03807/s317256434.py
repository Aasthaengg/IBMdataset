n = int(input())
a = list(map(int,input().split()))
if len([i for i in a if i % 2 == 1]) % 2 == 0:
  print("YES")
else:
  print("NO")