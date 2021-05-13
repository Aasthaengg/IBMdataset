h ,a =map(int,input().split())

y = h // a

if (h % a) > 0:
    y = y + 1

print(y)