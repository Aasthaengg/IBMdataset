import bisect
def find_min_fuka_idx(lst, x):
  ok = -1
  ng = len(lst)
  while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if x>=lst[mid]:
      ok = mid
    else:
      ng = mid
  return ng

a,b,q = map(int, input().split())
s = [-10**18]
s_mid = [int(input()) for i in range(a)]
s.extend(s_mid)
s.append(10**18)

t = [-10**18]
t_mid = [int(input()) for i in range(b)]
t.extend(t_mid)
t.append(10**18)

for i in range(q):
  x = int(input())
  si = bisect.bisect_right(s, x)
  tj = bisect.bisect_right(t, x)
  print(min(abs(x-s[si])+abs(s[si]-t[tj]),\
            abs(x-s[si])+abs(s[si]-t[tj-1]),\
           abs(x-t[tj])+abs(t[tj]-s[si]),\
            abs(x-t[tj])+abs(t[tj]-s[si-1]),\
            abs(x-s[si-1])+abs(s[si-1]-t[tj]),\
            abs(x-s[si-1])+abs(s[si-1]-t[tj-1]),\
           abs(x-t[tj-1])+abs(t[tj-1]-s[si]),\
            abs(x-t[tj-1])+abs(t[tj-1]-s[si-1])))
