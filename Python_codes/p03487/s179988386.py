from collections import Counter

n = int(input())
A = list(map(int,input().split()))

a_c = Counter(A)

ans = 0
for k,v in a_c.items():
    if k==v:
        continue
    if k>v:
        ans+=v
    if k<v:
        ans+=v-k
print(ans)  