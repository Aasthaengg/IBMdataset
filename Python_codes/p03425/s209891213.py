M = ['M', 'A', 'R', 'C', 'H']
m = [0]*5
result = 0
n = int(input())
for i in range(n):
    name = input()[0]
    if name in M:
        index = M.index(name)
        m[index] += 1

for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            result += m[i]*m[j]*m[k]
print(result)