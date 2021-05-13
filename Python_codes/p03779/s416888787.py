n = int(input())

ans = 0
c = 1
while True:
    ans += c
    if ans >= n:
        print(c)
        exit()
    c+= 1


