n = int(input())
a = list(map(int,input().split()))
a2 = [a[0]]
for i in range(n-1):
  a2.append(a2[i]+a[i+1])

ans = []

if n == 2:
  print(abs(a[0]-a[1]))
  exit()

for i in range(n-1):
  tmp = abs(a2[-1] - 2*a2[i])
  ans.append(tmp)
print(min(ans))