r, D, s = map(int, input().split())

def algae(r, D, x):
    return r*x -D

l = [s]
for i in range(1,11):
    xi = algae(r, D, l[i-1])
    l.append(xi)
    print(xi)