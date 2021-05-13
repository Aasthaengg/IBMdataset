s = int(input())
r = set([s])
n = s
while True:
    x = n//2 if n%2 == 0 else 3*n+1
    if x in r:
        print(len(r)+1)
        break
    r.add(x)
    n = x
