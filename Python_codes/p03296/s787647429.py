from itertools import groupby

n = int(input())
A = list(map(int,input().split()))

ans = 0
for key, group in groupby(A):
    ans += len(list(group))//2

print(ans)