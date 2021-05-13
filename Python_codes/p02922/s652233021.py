a,b=map(int,input().split())

tap = 1
ans = 0
while tap < b:
  tap += (a-1)
  ans += 1

print(ans)
