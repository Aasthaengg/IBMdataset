n = int(input())
a = [int(i) for i in input().split()]
a.insert(0,0)
a.append(0)

s = sum([abs(a[i] - a[i+1]) for i in range(len(a) - 1)])

for i in range(1, len(a)-1):
    tmp = s + abs(a[i-1] - a[i+1]) -(abs(a[i-1] - a[i]) + abs(a[i] - a[i+1]))
    print(tmp)