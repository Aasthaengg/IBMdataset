from itertools import count
X, Y = map(int, input().split())
for i in count(1):
    if 2**i*X > Y:
        print(i)
        break