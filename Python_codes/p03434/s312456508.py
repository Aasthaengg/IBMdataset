from sys import stdin
n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0

a.sort(reverse = True)

for x in range(n):
   if x % 2 == 0:
      ans += a[x]
   else:
      ans -= a[x]

print(ans)