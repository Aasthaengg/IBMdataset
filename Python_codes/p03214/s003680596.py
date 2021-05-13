import statistics
n = int(input())
a = list(map(int,input().split()))
s = statistics.mean(a)
c = float("inf")
for i in range(n):
    if c!=min(abs(s-a[i]),c):
        c = abs(s-a[i])
        d = i
print(d)