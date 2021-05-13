n , m = map(int, input().split())
count = 0
low = 0
high  = n
for _ in range(m):
    l,r=map(int, input().split())
    low = max(l, low)
    high = min(high, r)
    #print(low, high)

print(max(high-low+1, 0))