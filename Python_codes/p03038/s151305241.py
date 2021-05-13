n,m = map(int,input().split())
li = list(map(int,input().split()))
bc = [list(map(int,input().split())) for _ in range(m)]
 
li.sort()
bc.sort(key=lambda x:x[1],reverse=True)
l = []
l_len = 0
for b,c in bc:
    l += [c]*b
    l_len += b
    if l_len>n:
        break
    
ans = 0
for i in range(n):
    if i>=l_len:ans += li[i]
    else:ans += max(li[i],l[i])
print(ans)