n = int(input())
l, r = 0, n-1
print(0, flush=True)
l_s = input()
if l_s == "Vacant":
  exit()
print(n-1, flush=True)
l_t = input()
if l_t == "Vacant":
  exit()
while True:
  mid = (l+r)//2
  print(mid, flush=True)
  t = input()
  if t == "Vacant":
    exit()
  if ((mid-l)%2 and l_s==t) or ((mid-l)%2==0 and l_s!=t):
    r = mid
  else:
    l = mid
    l_s = t