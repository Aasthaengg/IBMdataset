import bisect
li = sorted(map(int, input().split()))
k = int(input())
for i in range(k):
    tmp = li.pop()
    bisect.insort(li, tmp * 2)
print(sum(li))