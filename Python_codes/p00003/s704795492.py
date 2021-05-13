n = int(raw_input())
for i in range(0, n):
    li = map(int, raw_input().split())
    li.sort()
    if li[0]**2 + li[1]**2 == li[2]**2:
        print 'YES'
    else:
        print 'NO'