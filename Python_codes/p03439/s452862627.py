N = int(input().strip())

print(0)
s0 = input().strip()
if s0 == "Vacant":
  exit()


def is_ok(arg):
  print(arg)
  s = input().strip()
  if s ==  "Vacant":
    exit()
  if (arg%2==0 and s==s0) or (arg%2!=0 and s!=s0):
    return True
  else:
    return False

def meguru_bisect(ng, ok):
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return print(ng)


ok = 0
ng = N-1
meguru_bisect(ng,ok)