n,k = map(int,input().split())
a = list(map(int,input().split()))
sun = sum(a)
cd = []
rcd = []
for i in range(1,int(sun**0.5)+1):
  if sun % i == 0:
    cd.append(i)
    rcd.append(sun//i)
rcd.reverse()
if cd[-1] == rcd[0]:
  del cd[-1]
gcd = cd + rcd
gcd.reverse()
count = 0
while True:
  g = gcd[count]
  b = list(map(lambda x: x%g, a))
  moon = sum(b) // g
  b.sort()
  luna = sum(b[:n-moon])
  if luna <= k:
    print(g)
    break
  count += 1