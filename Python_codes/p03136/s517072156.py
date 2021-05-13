n = int(input())

l = list(map(int,input().split()))
hen = 0
l.sort(reverse=True)

for x in range(1,n):
  hen += l[x]

if max(l) < hen:
  print("Yes")
else:
  print("No")