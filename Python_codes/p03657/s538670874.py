a = list(map(int, input().split()))
if a[0] % 3 == 0 or a[1] % 3 == 0 or sum(a[:2]) % 3 == 0:
    print("Possible")
else:
    print("Impossible")
