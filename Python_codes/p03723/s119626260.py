L = list(map(int, input().split()))
if L[0]%2 == 1 or L[1]%2 == 1 or L[2]%2 == 1:
    print(0)
    exit()

if (L[0]//2)%2 == 1 and (L[1]//2)%2 == 1 and (L[2]//2)%2 == 1:
    print(-1)
    exit()

i = 0
while True:
    i += 1
    L = [L[1]//2+L[2]//2, L[0]//2+L[2]//2, L[0]//2+L[1]//2]
    if L[0]%2 == 1 or L[1]%2 == 1 or L[2]%2 == 1:
        print(i)
        exit()
    if i >= 10**6:
        print(-1)
        exit()
