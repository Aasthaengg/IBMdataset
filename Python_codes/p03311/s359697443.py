import statistics
n = int(input())
a = list(map(int,input().split()))

bi = []
for i in range(n):
    bi.append(a[i]-i-1)

median = statistics.median(bi)

ans = 0
for i in range(n):
    ans += abs(a[i]-(median+i+1))
print(int(ans))