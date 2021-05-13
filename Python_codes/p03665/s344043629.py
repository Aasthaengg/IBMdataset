n, p, *a = map(int, open(0).read().split())
odd = [i for i in a if i%2 == 1]
if len(odd) == 0:
    if p == 0:
        print(2**n)
    else:
        print(0)
else:
    print(2**(n -1))