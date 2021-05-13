import bisect
n = int(input())
li = []
for i in range(100000):
    li.append(i**2)
a = bisect.bisect_right(li, n)
print(li[a-1])