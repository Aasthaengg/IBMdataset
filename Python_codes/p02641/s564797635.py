x, n = map(int, input().split())
p = list(map(int, input().split()))
cnt = 0
i = 0
while 1:
    if x - i not in p:
        print(x - i)
        break
    elif x + i not in p:
        print(x+i)
        break
    else:
        i += 1