a, b, c, k = map(int, input().split())
if k%2==0:
    if b-a < 10**18:
        print(a-b)
    else:
        print("Unfair")
else:
    if a-b < 10**18:
        print(b-a)
    else:
        print("Unfair")