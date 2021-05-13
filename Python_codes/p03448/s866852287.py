A = int(input())
B = int(input())
C = int(input())
X = int(input())

if A > 40:
	Amax = 40
else:
	Amax = A

ans = 0
for i in range(Amax+1):
	for j in range(B+1):
		for k in range(C+1):
			if 500*i + 100*j + 50*k == X:
				ans += 1

print(ans)