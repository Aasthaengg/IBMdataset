n = int(input())
for i in range(0, n+1, 7):
    for j in range(0, n+1, 4):
        if i + j == n:
            print('Yes')
            exit()
print('No')