N = int(input())
a = list(map(int, input().split()))
sunuke = 0
arai = sum(a)
p = []
for i in range(len(a)-1):
  sunuke += a[i]
  arai -= a[i]
  p.append(abs(sunuke - arai))

print(min(p))