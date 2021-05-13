def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def cmb(n, r):
	if n - r < r: r = n - r
	if r == 0: return 1
	if r == 1: return n

	numerator = [n - r + k + 1 for k in range(r)]
	denominator = [k + 1 for k in range(r)]

	for p in range(2,r+1):
		pivot = denominator[p - 1]
		if pivot > 1:
			offset = (n - r) % p
			for k in range(p-1,r,p):
				numerator[k - offset] /= pivot
				denominator[k] /= pivot

	result = 1
	for k in range(r):
		if numerator[k] > 1:
			result *= int(numerator[k])

	return result

n,m = map(int,input().split())
MOD = 10**9+7

l = factorization(m)

ans = 1

if m == 1:
	print(ans)
else:
	for _,c in l:
		ans = ans * cmb(c+n-1,c) % MOD

	print(ans)
