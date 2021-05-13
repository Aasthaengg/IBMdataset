mod = 10**9 + 7
n = int(input())
s = input()
dic = {}
for si in s:
  if si not in dic:
    dic[si] = 0
  dic[si] += 1
ans = 1
for k, v in dic.items():
  ans = ans * ((v+1) % mod) % mod
print((ans-1)%mod)