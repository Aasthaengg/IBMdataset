n = int(input())
a = sorted(map(int, input().split()), reverse=True)
t = 0
for i in range(n-1):
    t += a[i] - a[i+1]
print(t)