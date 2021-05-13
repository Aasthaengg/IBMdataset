a,b,c = list(map(int, input().split()))

if a%2==0 or b%2==0 or c%2==0:
    print(0)
    exit()

print(min(a*b, b*c, c*a))

