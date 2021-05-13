n,k = map(int,input().split())

l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])

l = sorted(l, key = lambda x:x[0])
cnt = 0    
for a,b in l:
    cnt += b
    
    if cnt >= k:
        print(a)
        break