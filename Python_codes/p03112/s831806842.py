import bisect
A, B, Q = map(int,input().split())
INF = 10**13

s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]

def get(x, s, t, ans_list):
  l_s = bisect.bisect_left(s, x)-1
  r_s = bisect.bisect_left(s, x)-1 + 1
  if l_s >= 0:
    y = s[l_s]
    l_t = bisect.bisect_left(t, y)-1
    r_t = bisect.bisect_left(t, y)-1 + 1
    if l_t >= 0:
      ans_list.append(abs(x-y) + abs(y-t[l_t]))
    if r_t <= len(t)-1:
      ans_list.append(abs(x-y) + abs(y-t[r_t]))
  if r_s <= len(s)-1:
    y = s[r_s]
    l_t = bisect.bisect_left(t, y)-1
    r_t = bisect.bisect_left(t, y)-1 + 1
    if l_t >= 0:
      ans_list.append(abs(x-y) + abs(y-t[l_t]))
    if r_t <= len(t)-1:
      ans_list.append(abs(x-y) + abs(y-t[r_t]))
  
  
for _ in range(Q):
  ans_list = []
  x = int(input())
  get(x, s, t, ans_list)
  get(x, t, s, ans_list)
  #print(x, ans_list)
  print(min(ans_list))
