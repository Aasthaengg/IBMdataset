k , t = map(int,input().split())
a = list(map(int,input().split()))
suma = sum(a)
maxa = max(a)

if suma - maxa >= maxa - 1:
    print(0)
else:
    print(maxa - 1 - (suma-maxa))