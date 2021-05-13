n = int(input())
a = input()
b = input()
c = input()

ans = 0
for i in range(n):
  h = [a[i], b[i], c[i]]
  h.sort()
  if h[0] != h[1] and h[1] != h[2]:
    ans += 2
  elif h[0] != h[2]:
    ans += 1
    
print(ans)