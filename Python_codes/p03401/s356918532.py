n = int(input())
a = [0] + list(map(int , input().split())) + [0]
#print(a)
d = 0
for i in range(len(a)):
    d += abs(a[i] - a[i-1])
#print(d)

for i in range(1, len(a)-1):
    x = d - abs(a[i] - a[i-1]) - abs(a[i+1] - a[i]) + abs(a[i+1] - a[i-1])
    print(x)


