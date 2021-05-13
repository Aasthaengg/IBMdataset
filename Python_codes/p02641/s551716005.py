x, n = map(int, input().split())

if n == 0:
    print(x)
    exit()

p = list(map(int, input().split()))

for d in range(x + 2):
    if x-d not in p:
        print(x-d)
        exit()
        
    if x+d not in p:
        print(x+d)
        exit()