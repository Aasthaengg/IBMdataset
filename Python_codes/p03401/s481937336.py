N = int(input())
a = [int(i) for i in input().split()]

a.insert(0,0)
a.append(0)

S = 0
for i in range(N+1):
    S += abs(a[i+1] - a[i])

for i in range(1,N+1):
    output = S + abs(a[i+1] - a[i-1]) - abs(a[i]-a[i-1]) - abs(a[i+1] - a[i])
    print(output)