#083_C
x, y = map(int, input().split())
z = y // x

for i in range(10**18):
    if x * pow(2,i) > y:
        print(i)
        break