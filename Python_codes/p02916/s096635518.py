n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
pnt = 0
cnt = -2
for i in a:
  if i == cnt+1:
    pnt += c[cnt-1]
  pnt += b[i-1]
  cnt = i
print(pnt)