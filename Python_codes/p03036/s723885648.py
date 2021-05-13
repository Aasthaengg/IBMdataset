r, D, x = map(int, input().split())
for i in range(1,11):
    print(round(r**i * (x+D/(1-r)) - D/(1-r)))