from math import floor

X = int(input())

res = 100
n = 0
while True:
    if res >= X:
        print(n)
        exit()
    res = (res * 101)//100
    n += 1