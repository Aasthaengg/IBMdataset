N = int(input())
A = list(map(int,input().split()))
ret = 0
def count(nega):
  ret = 0
  s = 0
  for e in A:
    nega = not nega
    #print(e,ret,s,s+e)
    if nega and 0 <= s + e:
      ret += abs(s + e) + 1
      s = -1
    elif not nega and s + e <= 0:
      ret += abs(s + e) + 1
      s = 1
    else:
      s += e
  return ret
print(min(count(True),count(False)))
