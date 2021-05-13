ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s,t = input().split()
a,b = nm()
u = input()

if u == s:
  a-=1
if u == t:
  b-=1

print(a)
print(b)