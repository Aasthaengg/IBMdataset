a, b = map(int, input().split())
for i in range(1, 13):
    if (a == i and i <= b) or (a == i+1 and b <= i):
        print(i)
