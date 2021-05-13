import sys

def main():
  input = sys.stdin.readline
  a, b, q = map(int, input().split())
  s = [0]*a
  for i in range(a):
    s[i] = int(input())
  
  t = [0]*b
  for i in range(b):
    t[i] = int(input())

  s_near = [0]*a
  k = 0
  for i in range(a):
    if k == b-1:
      s_near[i] = abs(s[i]-t[b-1])
      continue
    while True:
      sub = min([abs(s[i]-t[k]), abs(s[i]-t[k+1])])
      if sub == abs(s[i]-t[k+1]):
        k += 1
        if k == b-1:
          s_near[i] = sub
          break
        continue
      else:
        s_near[i] = sub
        break
  
  t_near = [0]*b
  k = 0
  for i in range(b):
    if k == a-1:
      t_near[i] = abs(t[i]-s[a-1])
      continue
    while True:
      sub = min([abs(t[i]-s[k]), abs(t[i]-s[k+1])])
      if sub == abs(t[i]-s[k+1]):
        k += 1
        if k == a-1:
          t_near[i] = sub
          break
        continue
      else:
        t_near[i] = sub
        break
  
  
  for i in range(q):
    x = int(input())
    if x <= s[0]:
      sub1 = s[0]-x+s_near[0]
    elif x >= s[a-1]:
      sub1 = x-s[a-1]+s_near[a-1]
    else:
      l, r = 0, a
      while r-l > 1:
        k = (r+l)//2
        if x <= s[k]:
          r = k
        else:
          l = k
      sub1 = min([s[r]-x+s_near[r], x-s[l]+s_near[l]])
    
    
    if x <= t[0]:
      sub2 = t[0]-x+t_near[0]
    elif x >= t[b-1]:
      sub2 = x-t[b-1]+t_near[b-1]
    else:
      l, r = 0, b
      while r-l > 1:
        k = (r+l)//2
        if x <= t[k]:
          r = k
        else:
          l = k
      sub2 = min([t[r]-x+t_near[r], x-t[l]+t_near[l]])
    ans = min([sub1, sub2])
    print(ans)


if __name__ == "__main__":
  main()