a,b,k = map(int, open(0).read().split())

for i in range(a,b+1):
    if abs(i-a)<k or abs(i-b)<k:
        print(i)