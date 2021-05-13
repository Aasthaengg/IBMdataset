n, y = list(map(int, input().split()))

for i in range(2000+1):
    for j in range(2000+1):
        if i*10000 + j*5000 + (n-i-j)*1000 == y and (n-i-j)>=0:
            print(str(i) + ' ' + str(j) + ' ' + str(n-i-j) + ' ')
            exit()
print('-1 -1 -1')