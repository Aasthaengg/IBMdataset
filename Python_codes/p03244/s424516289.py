n = int(input())
A = list(map(int, input().split()))

Aone = A[0]
counter = 0

for i in range (0, n):
	if A[i] == Aone:
		counter+=1
	else:
		break

if counter == n:
	print(int(n/2))
	exit()

k = int(len(A)/2)
maxA = max(A)

Odd = []
Even = []

for i in range (0, k):
	Odd.append(A[2*i])
	Even.append(A[2*i+1])

Oddcount = [0]*maxA
Evencount = [0]*maxA

for i in range (0, k):
	Oddcount[Odd[i]-1]+=1
	Evencount[Even[i]-1]+=1

Oddcount2 = sorted(Oddcount.copy())
Evencount2 = sorted(Evencount.copy())

if Oddcount.index(Oddcount2[-1]) != Evencount.index(Evencount2[-1]):
	print(2*k-Oddcount2[-1]-Evencount2[-1])
elif Oddcount2[-2] >= Evencount2[-2]:
	print(2*k-Oddcount2[-2]-Evencount2[-1])
else:
	print(2*k-Oddcount2[-1]-Evencount2[-2])