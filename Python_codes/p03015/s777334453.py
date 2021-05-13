#14:07
s = input()
l = len(s)
cnt = 0
ans = 0
mod = 10**9 + 7
di = [1]
tri = [1]
for _ in range(l):
  di.append(di[-1] * 2 % mod)
  tri.append(tri[-1] * 3 % mod)
#print(di)
#print(tri)
for i in range(l):
  if s[i] == '1':
    cnt += 1
    ans += tri[l-1-i] * di[cnt-1]
    ans %= mod
    #print(tri[l-1-i],di[cnt-1])
ans += di[cnt]
ans %= mod
print(ans)