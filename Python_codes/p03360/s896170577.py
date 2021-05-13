data = list(map(int, input().split()))
k = int(input())
if k == 1:
    print( sum(data) + max(data) )
else:
    tmp = max(data)
    for _ in range(k):
        tmp = tmp * 2
    print( sum(data) + tmp - max(data) )
