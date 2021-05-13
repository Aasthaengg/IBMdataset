N = int(input())
v = list(map(int,input().split()))

v = sorted(v, reverse = False)
def average(x,y):
    XY = (x + y) / 2
    return XY

gen = v[0]
for i in range(1,N):
    gen = average(gen ,v[i])

print(gen)    