n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

score = 0
for i in range(0, n):
   menu = a[i]
   score += b[menu-1]
   if i != 0 and a[i] - a[i-1] == 1:
      beforeMenu = a[i-1]
      score += c[beforeMenu-1]

print(score)