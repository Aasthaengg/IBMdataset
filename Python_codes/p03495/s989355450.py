from collections import Counter
n,k =list(map(int,input().split()))

a = list(map(int,input().split()))

c = Counter(a).most_common()
ans = 0
tmp = 0
for i,cnt in c:
    tmp += cnt
    k-=1
    if k == 0:
        ans = n-tmp
        break
print(ans)