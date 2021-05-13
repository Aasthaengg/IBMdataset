n,m = map(int,input().split())
a = list(map(int,input().split()))
sorted(a,reverse=True)
count = 0

for i in a:
    if i >=sum(a)/(4*m):
        count += 1
    else:
        pass

print(['No','Yes'][count >= m])

