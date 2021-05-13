X = int(input())

N = 200

for a in range(-N, N):
    for b in range(-N, N):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit(0)    
