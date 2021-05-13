n = int(input())
a = sorted(map(int,input().split()))[::-1]
print(sum([a[i]-a[i+1] for i in range(n-1)]))