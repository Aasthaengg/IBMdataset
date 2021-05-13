L = input()
N = len(L)

MOD = 10 ** 9 + 7

if L[0] == "1":
  e = [2]
  l = [1]
else:
  e = [1]
  l = [0]
  
for i in range(1, N):
  if L[i] == "1":
    de = (e[-1] * 2) % MOD
    dl = (e[-1] * 1 + l[-1] * 3) % MOD
  else:
    de = (e[-1] * 1) % MOD
    dl = (e[-1] * 0 + l[-1] * 3) % MOD
  e.append(de)
  l.append(dl)
#print("e:", e)
#print("l:", l)
print((e[-1] + l[-1]) % MOD)