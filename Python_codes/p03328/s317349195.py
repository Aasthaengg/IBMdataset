v = []
sums = 1
for i in range(2,1010):
    v.append(sums)
    sums += i
a,b = map(int,input().split())
for i in range(1000):
    if v[i] - a == v[i+1] - b:
        print(v[i] - a)
        break