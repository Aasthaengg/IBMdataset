def num(v):
	try:
		return int(v)
	except Exception:
		return v

ALL_calc = []
while True:
	N =  input().split(' ')
	if N[1] == '?':
		break
		
	N_calc = []
	for i in range(len(N)):
		N_calc.append(num(N[i]))
	ALL_calc.append(N_calc)
	
for i in range(len(ALL_calc)):
	if ALL_calc[i][1] == '+':
		print(ALL_calc[i][0] + ALL_calc[i][2])
	elif ALL_calc[i][1] == '-':
		print(ALL_calc[i][0] - ALL_calc[i][2])
	elif ALL_calc[i][1] == '*':
		print(ALL_calc[i][0] * ALL_calc[i][2])
	elif ALL_calc[i][1] == '/':
		print(ALL_calc[i][0] // ALL_calc[i][2])