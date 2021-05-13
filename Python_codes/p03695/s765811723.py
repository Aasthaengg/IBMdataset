import bisect

n = int(input())
a = list(map(int,input().split()))
a.sort()
sect = 0
col = 0
for i in range(400,3201,400):
    nsect = bisect.bisect_left(a,i)
    if nsect>sect:
        sect = nsect
        col += 1
print(max(col,1),col+n-nsect)