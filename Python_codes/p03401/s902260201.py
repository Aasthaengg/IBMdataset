import copy
n = int(input())
a = [0] + list(map(int, input().split())) + [0]
cost = 0
for i in range(n+1):
    cost += abs(a[i]-a[i+1])
for i in range(1, n+1):
    ans = copy.deepcopy(cost)
    if a[i-1] <= a[i] and a[i+1] <= a[i]:
        ans -= 2*abs(a[i]-max(a[i-1], a[i+1]))
    elif a[i-1] >= a[i] and a[i+1] >= a[i]:
        ans -= 2*abs(a[i]-min(a[i-1], a[i+1]))
    print(ans)