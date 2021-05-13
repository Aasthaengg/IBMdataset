n = int(raw_input())
ais = map(int, raw_input().split(' '))
cumul = [0,1]
"""
a    b
15 = 6 x 2 + 3
b    a%b

a    b       a%b
6  = 3 x 1 + 0
b    a%b

a   b
3   0

"""
def gcd(a,b):
	return gcd(b, a % b) if b else a
	#return a if a else gcd(b, a % b)
for a in ais:
	b,c = cumul
	#1c   ab
	#ac   ac

	cumul = [c + a*b, a*c]
	g = gcd(cumul[0], cumul[1])
	cumul = [cumul[0]/g, cumul[1]/g ]

print float(cumul[1])/cumul[0]