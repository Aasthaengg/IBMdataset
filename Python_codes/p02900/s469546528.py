import fractions
a,b=map(int,input().split())

g=fractions.gcd(a,b)
org=g
counter=1
for i in range(2,int(g**0.5)+1):
	if g%i == 0:
		counter += 1
		g //= i
		while g % i ==0:
			g //= i

if g > int(org ** 0.5):
	counter += 1

print(counter)

