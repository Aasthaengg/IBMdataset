n,m = map(int,input().split())

menu = [i for i in range(1,m+1)]
cnt = [0]*m
a = []

for i in range(n):
    ka = list(map(int,input().split()))
    ka.pop(0)
    a.append(ka)
    
for i in menu:
    for j in a:
        if i in j:
            cnt[i-1] += 1
            
print(cnt.count(n))