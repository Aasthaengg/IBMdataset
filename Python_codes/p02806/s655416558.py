n = int(input())
ans = 0
s = [list(map(str,input().split())) for i in range(n)]
key_s = str(input())
key = 0
for t,tt in s:
  if key == 1:
    ans += int(tt)
  if t == key_s:
    key = 1
print(ans)
    
