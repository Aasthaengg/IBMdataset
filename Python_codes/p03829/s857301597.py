#7 1 100
#40 43 45 105 108 115 124
n,a,b = map(int, raw_input().split())
xis = map(int ,raw_input().split())
cost = 0
for u,v in zip(xis,xis[1:]):
	cost += min((v-u)*a, b)
print cost 