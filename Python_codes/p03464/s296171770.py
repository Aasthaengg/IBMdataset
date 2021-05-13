mn = 2
mx = 2
n = int(input())
k = [int(i) for i in input().split()]
k.reverse()
for i in range(n):
  t1 = (mn + k[i] - 1) // k[i] * k[i]
  t2 = (mx) // k[i] * k[i]
  if t1 > mx:
    print(-1)
    exit()
  mn = t1
  mx = t2 + k[i] - 1
print(mn, mx)