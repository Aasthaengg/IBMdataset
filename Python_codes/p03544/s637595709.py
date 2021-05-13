n = int(input())

l = [0]*(n+1)
l[0] = 2
l[1] = 1

def luca (x:int):
    if l[x] > 0:
        return l[x]
    else:
        l[x] = luca(x-1) + luca(x-2)
        return l[x]

print (luca(n))
