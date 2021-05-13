from sys import exit
from random import randrange
MOD = 10**9+7
n, k = map(int, input().split())
b = list(map(int, input().split()))
a = []
if n == k:
	ans = 1
	for x in b:
		ans *= x
		ans %= MOD
	print(ans)
	exit()
for x in b:
	if x != 0:
		a.append(x)
if len(a) < k:
	print(0)
	exit()

a.sort(key=lambda x: -abs(x))
#print(a)
ans = 1
minus = 0
for i in range(k):
	ans *= a[i]
	ans %= MOD
	if a[i] < 0:
		minus += 1

if minus%2 == 0:
	print(ans)
	exit()

if len(a) == k:
	if len(a) < n:
		print(0)
		exit()

for i in range(k, len(a)):
	if a[i] < 0:
		minus += 1

if minus == len(a):
	if len(a) < n:
		print(0)
		exit()
	ans = 1
	for i in range(k):
		ans *= a[-i-1]
		ans %= MOD
	print(ans)
	exit()

flg1 = False
for i in range(k-1, -1, -1):
	if a[i] * a[k] < 0:
		p, q = a[i], a[k]
		flg1 = True
		break

flg2 = False
for i in range(k, len(a)):
	if a[k-1] * a[i] < 0:
		r, s = a[k-1], a[i]
		flg2 = True
		break

if flg1 and flg2:
	if abs(q*r) >= abs(p*s):
		ans *= pow(p, MOD-2, MOD)
		ans *= q
		print(ans%MOD)
	else:
		ans *= pow(r, MOD-2, MOD)
		ans *= s
		print(ans%MOD)

elif flg1:
	ans *= pow(p, MOD-2, MOD)
	ans *= q
	print(ans%MOD)

elif flg2:
	ans *= pow(r, MOD-2, MOD)
	ans *= s
	print(ans%MOD)

else:
	print("コーナーケース多すぎん？")