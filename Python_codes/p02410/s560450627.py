n, m = map(int, input().split())
gyoretu = [[0 for i in range (m)] for j in range(n)]
vector = [] #?¨?????????????
vector2 = [0 for i in range(n)] #?¨?????????????

for i in range(n):
	#for j in range(m):
	gyoretu[i] = input().split()
	#print(gyoretu[i][1])

for j in range(m):
    vector.append(int(input()))

#calculate
for i in range(n):
	for j in range(m):
		vector2[i] += int(gyoretu[i][j])*int(vector[j])

for i in range(n): 
	print(vector2[i])