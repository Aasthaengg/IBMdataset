ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,m,x = nm()
a=nl()

left=0
right=0
for ai in a:
  if ai < x:
    left+=1
  if ai > x:
    right+=1
print(min(left,right))