import collections
N = int(input())
A = list(map(int,input().split()))
C = collections.Counter(A)
ans = 0
for key in C.keys():
    if key > C[key]:
        ans += C[key]
    elif key < C[key]:
        ans += C[key]-key
print(ans)