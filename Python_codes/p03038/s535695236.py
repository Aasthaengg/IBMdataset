n,m = map(int,input().split())
li = list(map(int,input().split()))
bc = [list(map(int,input().split())) for _ in range(m)]

bc.sort(key=lambda x:x[1],reverse=True)
l = []
ans = 0

for b,c in bc:
    l += [c]*b
    if len(l) > n:
        break
    
li += l
li.sort(reverse=True)
print(sum(li[:n]))
