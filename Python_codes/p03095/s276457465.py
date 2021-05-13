n = int(input())
s = input()
dic = {}
for i in range(n):
  if s[i] in dic:
    dic[s[i]] += 1
  else:
    dic[s[i]] = 1
ans = 1
for v in dic.values():
  ans *= (1 + v)
  ans %= 10**9 + 7
ans -= 1
print(ans)