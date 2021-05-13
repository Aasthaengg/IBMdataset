N = int(input())
a = list(map(int,input().split()))
a = sorted(a)
k = 10**6

for i in range(a[0],a[-1]+1):
  total = 0
  for s in a:
    total +=(i-s)**2
  #print(total)
  k = min(k,total)
print(k)  