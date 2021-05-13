n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

length = len(format(a[-1],'b'))
string = '0'+str(length)+'b'

ans = 0
while True:
	k_length = len(format(k,'b'))
	if length < k_length:
		ans += n * (2**(k_length - 1))
		k -= 2**(k_length - 1)
	else:
		break

l = [0 for _ in range(length)]

for i in range(len(a)):
	tmp = tuple(format(a[i],string))
	for j in range(length):
		if tmp[j] == '0':
			l[j] += 1

res = '0b'
num = 0
tmp = 2 ** length
for i in range(len(l)):
	tmp //= 2
	if l[i] > n // 2 and num + tmp <= k:
		res = res + '1'
		num += tmp
	else:
		res = res + '0'

x = int(res,2)

for i in range(len(a)):
	ans += x ^ a[i]
print(ans)
