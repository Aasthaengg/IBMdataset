n, m, l = map(int, input().split())

nm = []
ml = []

for _ in range(n):
	lista = list(map(int, input().split()))
	nm.append(lista)

for _ in range(m):
	lista = list(map(int, input().split()))
	ml.append(lista)
	
matrix = []

for i in range(n):
	lista = []
	for j in range(l):
		sum = 0
		for k in range(m):
			sum += nm[i][k]*ml[k][j]
		lista.append(sum)
	matrix.append(lista)

for i in range(n):
	text = ""
	for j in range(l):
		text += str(matrix[i][j]) + " "
	print(text[:-1])