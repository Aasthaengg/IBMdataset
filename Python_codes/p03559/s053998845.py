import bisect

a = int(input())
b = list(map(int, input().split()))
b.sort()
c = list(map(int, input().split()))
d = list(map(int, input().split()))
d.sort()
e = 0
for i in c:
    e += bisect.bisect_left(b, i) * (a - bisect.bisect_right(d, i))
print(e)
