ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

d,n = nm()

if n == 100:
  n+=1
ans = n*100**d
print(ans)