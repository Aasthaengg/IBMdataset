
c,n = 0,int(raw_input())
def check(v,n):
	return v and n/v == n%v

for d in range(1, (int(n **0.5) +1)):
	if n % d == 0:
		for v in set([d, n/d]):
			if check(v-1,n):
				c += v-1

print c