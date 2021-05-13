n = int(input())
a = list(map(int, input().split())) 

half = sum(a)/2
l, r, i = 0, a[0], 0

while r < half:
    i += 1
    l = r
    r += a[i]

print(int(min(half - l, r - half)*2 ))