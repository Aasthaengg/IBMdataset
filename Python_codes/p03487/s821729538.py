import collections
N = int(input())
a = list(map(int,input().split()))
B = collections.Counter(a)
ans = 0
for i in set(a):
    if B[i] < i:
        ans += B[i]
    else:
        ans += B[i]-i
print(ans)