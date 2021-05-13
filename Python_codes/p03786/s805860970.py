n = int(input())
aa = list(map(int, input().split()))
animals = sorted(aa)

ind = 0
s = animals[0]
for i, a in enumerate(animals[:-1]):
    if animals[i+1] > 2*s:
        ind = i+1
    s += animals[i+1]
print(n-ind)
