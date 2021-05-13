c = []
for i in range(3):
    c.append(list(map(int, input().split())))

for i in range(2):
    for j in range(2):
        if c[j][i+1] - c[j][i] != c[j+1][i+1] - c[j+1][i]:
            print('No')
            exit()
print('Yes')