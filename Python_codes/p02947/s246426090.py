N = int(input())
ls = {}
ans = 0

for i in range(N):
  s = input()
  ns = ''.join(sorted(s))
  if ns in ls:
    ans += ls[ns]
    ls[ns] += 1
  else:
    ls[ns] = 1
    
print(ans)