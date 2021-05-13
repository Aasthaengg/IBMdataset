n,k = map(int,input().split())
s = str(input())
s += "2"
if int(s[0]) == 0:
  a = [0]
  prev = "0"
  count = 1
else:
  a = []
  flag = False
  prev = "1"
  count = 1
ap = a.append
for i in range(1,n+1):
  if s[i] == prev:
    count += 1
  else:
    ap(count)
    count = 1
    prev = s[i]
if s[-2] == "0":
  ap(0)
if 2*k+1 >= len(a):
  print(sum(a))
  exit()
g = sum(a[0:2*k+1])
mx = g
i = 1
while 2*i+2*k < len(a):
  g -= (a[2*i-2]+a[2*i-1])
  g += (a[2*i+2*k-1]+a[2*i+2*k])
  if g > mx:
    mx = g
  i += 1
print(mx)