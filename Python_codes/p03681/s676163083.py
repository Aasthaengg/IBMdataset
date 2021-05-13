n,m=map(int,input().split())

p = 10 ** 9 + 7
N = 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
	fact.append((fact[-1] * i) % p)
	inv.append((-inv[p % i] * (p // i)) % p)
	factinv.append((factinv[-1] * inv[-1]) % p)

if n==m:
	#2つ交互にならべる
	#oxoxoxoxoxox...ox これを2倍したのが答え.
	print(fact[n]*fact[n]*2 % p)
elif n+1==m:
	#犬が1匹多い
	#oxoxoxoxox....oxo.
	print(fact[n]*fact[m] % p)
elif n==m+1:
	print(fact[n]*fact[m] % p)
else:
	print(0)