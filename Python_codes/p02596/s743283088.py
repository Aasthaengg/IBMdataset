K = int(input())
ans = '-1'
mod = 7%K
path = [mod]
for i in range(1,K+1):
  if mod == 0:
    ans = i
    break
  mod = (mod*10 + 7)%K
  path.append(mod)
  if mod == path[0]:
    ans = '-1'
    break
print(ans)
