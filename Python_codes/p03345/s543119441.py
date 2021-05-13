a,b,c,k = map(int, open(0).read().split())

fact = 1
if k%2:
    fact = -1
print((a-b)*fact)