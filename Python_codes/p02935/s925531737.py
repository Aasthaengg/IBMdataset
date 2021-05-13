N = int(input())
v = list(map(int, input().split()))

v.sort()
total = v[0]
for i in range(1, len(v)):
    total = (total + v[i]) / 2
    
print(total)