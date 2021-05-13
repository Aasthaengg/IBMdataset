a = int(input())
s =list(map(int,input().split()))
mod = 10 **18
ans = 1
if 0 in s:
    print(0)
    exit()
for i in s:
    ans = ans *i
    if ans > 1e18:
      print(-1)
      exit()
print(ans)

