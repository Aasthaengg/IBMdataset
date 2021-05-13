a, b = map(int,input().split())

if a < b:
    a, b = b, a

b = str(b)

print(b*a)