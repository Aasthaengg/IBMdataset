x = int(input())
q,r = divmod(x, 100)
if r <= q*5:
    print(1)
else:
    print(0)