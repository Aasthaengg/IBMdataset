n,h = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

a_max = max(a for a,b in AB)
B = [b for a,b in AB if b>a_max]
B.sort(reverse=True)
ans = 0

for b in B:
    if h<=0:
        break
    ans+=1
    h-=b
if h>0:
    ans+=(h+a_max-1)//a_max
print(ans)