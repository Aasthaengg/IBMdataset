from collections import Counter

n = int(input())
a = [int(input()) for _ in range(n)]
cnt = Counter(a)
ans=0
for val in set(a):
    if cnt[val]%2!=0:
        ans+=1
print(ans)