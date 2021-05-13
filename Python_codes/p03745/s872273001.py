n = int(input())
if n>1: a = list(map(int, input().split()))
else: a = int(input()); print(1); exit()
ans = 1; togU = 0; togD = 0
if a[1]>a[0]: togU = 1
elif a[1]<a[0]: togD = 1
for i in range(1,n):
  if not (togD or togU):
    if a[i]>a[i-1]: togU = 1; continue
    if a[i]<a[i-1]: togD = 1; continue
  if a[i]>a[i-1]:
    if togD:
      ans += 1
      togD = 0
      togU = 0
  elif a[i]<a[i-1]:
    if togU:
      ans += 1
      togU = 0
      togD = 0
print(ans)