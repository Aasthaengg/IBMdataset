n = int(input())
xs = list(map(int, input().split()))
xs = [0] + xs + [0]

total = 0

for i in range(1,n+2):
    total += abs(xs[i]-xs[i-1])

for j in range(1,n+1):
    print(total-abs(xs[j]-xs[j-1])-abs(xs[j]-xs[j+1])+abs(xs[j-1]-xs[j+1]))
