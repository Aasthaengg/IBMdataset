X = int(input())
A = 0
B = 0
for i in range(1,10**5):
    if A < X:
        A+=i
    else:
        print(i-1)
        exit()