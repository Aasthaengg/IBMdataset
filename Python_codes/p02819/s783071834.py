X = int(input())
while True:
    prime = True
    for i in range(2, int(X**0.5)+1):
        if X % i == 0:
            prime = False
            break
    if prime:
        print(X)
        exit()
    X += 1
