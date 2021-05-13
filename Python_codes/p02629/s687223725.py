n = int(input())
k = 26
p = 1
while (n > k):
	n -= k
	k *= 26
	p += 1
k = 26 ** (p - 1)
s = ""
n -= 1
while (k):
	s += chr(ord('a') + n // k)
	n %= k
	k //= 26
print(s)
# print(p, n)