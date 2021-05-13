X, N = map(int, input().split())
p = list(map(int, input().split()))


if N == 0:
    print(X)
    exit()

for i in range(102):
    if X - i not in p:
        print(X - i)
        exit()
    
    if X + i not in p:
        print(X + i)
        exit()
