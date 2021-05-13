ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

ans = 0

for i in range(n):
  while a[i]%2==0:
    a[i]//=2
    ans+=1

print(ans)