n = int(input())
kaidan = [1]
for i in range(2,int((2*n)**0.5+1)):
    kaidan.append(kaidan[-1]+i)
if not n in kaidan:
    print("No")
    exit()
print("Yes")
size = kaidan.index(n)+1
print(size+1)
hyo = [[0 for i in range(size)] for j in range(size)]
for i in range(size):
    for j in reversed(range(i+1)):
        hyo[i][j] = kaidan[i] - (i - j)
        hyo[j][i] = hyo[i][j]
kar = []
for i in range(size):
    kar.append(hyo[i][i])
hyo.append(kar)

for i in range(size+1):
    print(size,end=" ")
    print(*hyo[i])