n = int(input())
x = n // 4
for i in range(x+1):
    for j in range(x+1):
        if n == 4*i + 7*j:
            print('Yes')
            exit()

print('No')