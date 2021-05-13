X = int(input())

if X in (1, 2):
    print(X)
    exit()

for i in range(2, 10**5):
    a = i * (i+1) / 2
    if a - (i-1) <= X <= a:
        print(i)
        exit()
