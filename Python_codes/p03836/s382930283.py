Sx, Sy, Tx, Ty = map(int, input().split())

Takasa = Ty-Sy
Haba = Tx-Sx

Ito = []

for i in range (0, Takasa):
	Ito.append('U')

for i in range (0, Haba):
	Ito.append('R')

for i in range (0, Takasa):
	Ito.append('D')

for i in range (0, Haba+1):
	Ito.append('L')

for i in range (0, Takasa+1):
	Ito.append('U')

for i in range (0, Haba+1):
	Ito.append('R')

Ito.append('DR')

for i in range (0, Takasa+1):
	Ito.append('D')

for i in range (0, Haba+1):
	Ito.append('L')

Ito.append('U')

print(*Ito, sep='')