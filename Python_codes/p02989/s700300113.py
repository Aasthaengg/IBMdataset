a=int(input())
b=list(map(int,input().split()))
b.sort()
if b[int(a/2)-1]==b[int(a/2)]:
  print(0)
else:
  print(b[int(a/2)]-b[int(a/2)-1])