n = int(input())
a = list(map(int, input().split())) 

mm = 10**18
s = sum(a)
l, r = 0, 0

for i in range(n):
    l += a[i]
    r = s - l
    mm = min(mm, abs(l-r))

print(mm)

