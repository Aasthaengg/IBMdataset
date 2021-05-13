from collections import Counter
n = int(input())
c = Counter([''.join(sorted(input())) for i in range(n)])
 
ans = 0
for k, cnt in c.items():
    ans+=cnt*(cnt-1)//2
print(ans)