import fractions

N=int(input())
A=list(map(int, input().split()))
gcdans=A[0]
for i in range(1,N):
	gcdans=fractions.gcd(gcdans,A[i])

print(gcdans)
