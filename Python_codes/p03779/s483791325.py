X = int(input())
pos = 0
for i in range(1, 100001):
    pos += i
    if pos >= X:
        print(i)
        break
