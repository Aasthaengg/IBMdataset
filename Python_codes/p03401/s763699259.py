n = int(input())
a = [int(x) for x in input().split()]
a.append(0)
a.insert(0,0)
sm = 0

for i in range(1,len(a)):
    sm += abs(a[i] - a[i-1])

for i in range(1,len(a)-1):
    dis1 = abs(a[i-1] - a[i]) + abs(a[i+1] - a[i])
    dis2 = abs(a[i-1] - a[i+1])
    print(sm - dis1 + dis2)
