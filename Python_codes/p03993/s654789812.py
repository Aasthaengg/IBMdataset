from collections import defaultdict
n=int(input())
a=[int(i) for i in input().split()]

dic = defaultdict(set)
ans=0
for i in range(n):
    dic[a[i]].add(i+1)
    if a[i] in dic[i+1]:
        ans+=1
print(ans)