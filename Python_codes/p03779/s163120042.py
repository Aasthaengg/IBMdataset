X = int(input())
for i in range(X+1):
    if i * ( i + 1 ) // 2 >= X:
        print(i)
        exit()
