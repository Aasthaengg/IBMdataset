n = int(input())
ll = list(map(int,input().split()))
li = [l-i for i,l in enumerate(ll)]
import statistics
median = statistics.median(li)
ans = 0
for l in li:
    ans+= abs(l-median)
print(int(ans))