n =int(input())
a = list(map(int,input().split()))
b = sorted(a)
if b[len(a)//2-1] != b[len(a)//2]:
  print(b[len(a)//2]-b[len(a)//2-1])
else:
  print(0)