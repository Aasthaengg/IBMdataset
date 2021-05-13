import collections

N = int(input())
A = list(map(int,input().split()))

B = collections.Counter(A)
#print(B)

C = list(B.keys())
#print(C)

ans = 0
for c in C:
    if c != B[c] and B[c] > c:
        ans += B[c]-c
    elif c != B[c] and B[c] < c:
        ans += B[c]
print(ans)