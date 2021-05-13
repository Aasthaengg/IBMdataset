n,c,k = map(int,input().split())
l = sorted(list(int(input()) for _ in range(n)))
bus = 1
now = 1
time = l[0]+k
for i in range(1,n):
  b = l[i]
  if b<=time and time<=b+k and now<c:
    now += 1
  else:
    bus += 1
    now = 1
    time = l[i]+k
print(bus)