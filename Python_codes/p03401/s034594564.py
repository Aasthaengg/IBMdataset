n = int(input())
*a, = map(int, input().split())

a.insert(0, 0)
a.append(0)

s = 0
for i in range(len(a)-1):
    s += abs(a[i]-a[i+1])

for i in range(1, len(a)-1):
    print(s + abs(a[i-1]-a[i+1]) - (abs(a[i-1]-a[i]) + abs(a[i]-a[i+1])))
