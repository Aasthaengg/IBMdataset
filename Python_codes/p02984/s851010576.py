n = int(raw_input())
ais = map(int,raw_input().split(' '))
res = [0] * n

c = 0
sign = 1
for ai in ais:
	c += ai * sign
	sign *= -1
res[0] = c/2
for i in range(1, len(ais)): res[i] = ais[i-1] - res[i-1]
print ' '.join(map(str,[e*2 for e in res]))