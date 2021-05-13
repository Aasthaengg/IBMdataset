r = int(input())
g = int(input())

n = -r
while True:
    x = (r + n) / 2
    if x == g:
        print(n)
        break
    n += 1