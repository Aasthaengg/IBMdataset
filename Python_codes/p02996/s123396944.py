n = int(input())
ab = [tuple(map(int,input().split())) for i in range(n)]
ab.sort(key = lambda x:x[1])

t = 0
for a,b in ab:
    t +=a
    if t > b:
        print('No')
        exit()
print('Yes')