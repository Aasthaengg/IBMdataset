N=int(input())
v=list(map(int,input().split()))

for i in range(N-1):
    x = min(v)
    v.remove(x)
    y = min(v)
    v.remove(y)
    z = (x+y)/2
    v.append(z)
    #print(v)

print(v[-1])
