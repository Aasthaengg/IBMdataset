N=int(input())
d={}

for i in range(N):
    a=int(input())
    d[a] = not(d.get(a, 0))
print(sum(d.values()))