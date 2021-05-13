import sys

n = int(input())
l = 0
r = n-1
mid = r // 2
re = [None] * n
print(0, flush=True)
re[0] = input()
if re[0] == "Vacant":
  sys.exit()
print(n-1, flush=True)
re[n-1] = input()
if re[n-1] == "Vacant":
  sys.exit()
print(mid, flush=True)
re[mid] = input()
while re[mid] != "Vacant":
  if re[l] == re[mid]:
    if (mid - l) % 2:
      r = mid
    else:
      l = mid
  else:
    if (mid - l) % 2:
      l = mid
    else:
      r = mid
  mid = (l + r) // 2
  print(mid, flush=True)
  re[mid] = input()
else:
  sys.exit()
