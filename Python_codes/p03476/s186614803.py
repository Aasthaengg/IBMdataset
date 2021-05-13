import bisect

def sieve(n):
	ret = []
	divlis = [-1]*(n+1)  # 何で割ったかのリスト(初期値は-1)
	flag = [True]*(n+1)
	flag[0] = False
	flag[1] = False
	ind = 2
	while ind <= n:
		if flag[ind]:
			ret.append(ind)
			ind2 = ind**2
			while ind2 <= n:
				flag[ind2] = False
				divlis[ind2] = ind
				ind2 += ind
		ind += 1
	#何で割ったかのリストを取得したいとき, divlisも出力する
	return ret

svl = set(sieve(10**5))
ansl = []

for i in svl:
	if i * 2 - 1 in svl:
		ansl.append(i*2-1)

ansl.sort()

q = int(input())

for _ in range(q):
	l, r = map(int,input().split())
	ans = bisect.bisect_right(ansl, r) - bisect.bisect_left(ansl, l)
	print(ans)