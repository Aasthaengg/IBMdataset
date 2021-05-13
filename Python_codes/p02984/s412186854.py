ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a=nl()

ans = [0]
for i in range(n): 
  if i%2==0:
    ans[0]+=a[i]
  else:
    ans[0]-=a[i]

print(ans[0])
for i in range(1,n):
  an = 2*a[i-1]-ans[i-1]
  print(an)
  ans.append(an)
