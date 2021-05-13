n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

s = 0
num = 0
if x>sum(a):
  print(len(a)-1)
else:
  for i in range(len(a)):
      if x >= a[i]:
          x -= a[i]
          num += 1
      else:
          break

  print(num)
