K = int(input())
A = list(map(int, input().split()))[::-1]
if A[0] != 2:
  print(-1)
  quit()

left = 2; right = 3
for a in A[1:]:
  ra = right - right%a
  if ra < left:
    print(-1)
    quit()
  l1 = ra; r1 = ra + a - 1
  la = left + (a - (left%a))%a
  l2 = la; r2 = la + a - 1
  left = min(l1, l2)
  right = max(r1, r2)

print(left, right)