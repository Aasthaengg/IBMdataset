N = int(input())
a = list(map(int,input().split()))

a.sort(reverse = True)

diff = 0
for i in range(N):
  diff += ((-1) ** i) * a[i]

print(diff)