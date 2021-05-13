n = int(input())

print(0)
lf = input()
if lf == "Vacant":
    exit()

print(n-1)
rf = input()
if rf == "Vacant":
    exit()
l = 0
r = n-1

while True:
    k = (l+r)//2
    print(k)
    f = input()
    if f == "Vacant":
        exit()
    else:
        if (abs(r-k) % 2 == 1 and rf == f) or (abs(r-k) % 2 == 0 and rf != f):
            l = k
            lf = f
        elif (abs(l-k) % 2 == 1 and lf == f) or (abs(l-k) % 2 == 0 and lf != f):
            r = k
            rf = f