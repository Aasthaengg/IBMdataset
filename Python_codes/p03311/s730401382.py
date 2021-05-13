n = int(input())
a = list(map(int,input().split()))
b = [a[i]-i for i in range(n)]
x = sorted(b)[n//2]
sadness = 0
for i in range(n):
    sadness += abs(a[i]-i-x)
print(sadness)