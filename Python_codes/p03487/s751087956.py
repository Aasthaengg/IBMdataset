import collections

n = int(input())
a = [int(i) for i in input().split()]
b = collections.Counter(a)
ans =0
for i,n in b.items():
    if i > n:
        ans += n
    else:
        ans += abs(n-i)
print(ans)