import copy

n = int(input())
l = list(map(int,input().split()))
p1 = n//2
p2 = n//2-1
ans = copy.copy(l)
ans.sort()

for i in l:
    if i >= ans[p1]:
        print(ans[p2])
    else:
        print(ans[p1])
