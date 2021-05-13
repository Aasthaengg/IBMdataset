n = int(input())
if n == 1:
    print(1)
else:
    L = [None] * 100
    L[0] = 2
    L[1] = 1
    for i in range(2, 87):
        L[i] = L[i-1] + L[i-2]
        if i == n: 
            print(L[i])
            exit()