n = int(input())
def com(call):
  print(call)
  res = input()
  if res == "Vacant":
    exit(0)
  return res

resp = [None]*n
resp[0] = com(0)
resp[n-1] = com(n-1)

l = 0
r = n-1
while r-l>1:
  mid = (r+l)//2
  resp[mid] = com(mid)
  if ((r-mid)%2)==(resp[r]==resp[mid]):
    l = mid
  else:
    r = mid
com(l)
com(r)