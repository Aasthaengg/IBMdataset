from itertools import combinations
n = int(input())
lst = [(i+1) for i in range(n)]
ans = []
for x,y in combinations(lst, 2):
    if n%2==0:
        if x+y==n+1:
            continue
    if n%2!=0:
        if x+y==n:
            continue
    ans.append((x,y))
print(len(ans))
for x,y in ans:
    print(x,y)