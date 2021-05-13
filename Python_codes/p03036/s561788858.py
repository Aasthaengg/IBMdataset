# B
r, d, x = map(int, input().split())
xi = [[] for i in range(11)]
xi[0] = x
for i in range(10):
    xi[i + 1] = xi[i] * r - d
xi = xi[1:11]
print(*xi, sep='\n')
