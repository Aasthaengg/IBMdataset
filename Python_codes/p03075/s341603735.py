d = []
for i in range(5):
    d.append(int(input()))
k = int(input())
for i, j1 in enumerate(d[:5]):
    for j2 in d[i+1:]:
        if (j1 - j2) ** 2 > k ** 2:
            print(':(')
            exit()
print('Yay!')