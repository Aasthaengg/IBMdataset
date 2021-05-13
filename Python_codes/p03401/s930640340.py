N = int(input())
a = list(map(int,(input().split())))
a.insert(0,0)
a.append(0)
cost = 0
now = 0
for i in range(1,N+2):
    cost += abs(now-a[i])
    now = a[i]

for i in range(1,N+1):
    if (a[i]-a[i-1])*(a[i+1]-a[i]) < 0:
        if (a[i]-a[i-1])*(a[i+1]-a[i-1]) >= 0:
            print(cost-(abs(a[i+1]-a[i])*2))
        else:
            print(cost-(abs(a[i]-a[i-1])*2))
    else:
        print(cost)