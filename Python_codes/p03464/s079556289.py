k = int(input())
l = reversed(list(map(int, input().split())))
lo,hi = 2,2
for a in l:
  nl = lo + (a - lo%a)%a
  nh = (hi//a)*a + a-1
  if nl > nh: print(-1); exit(0)
  lo,hi = nl,nh
print(lo,hi)