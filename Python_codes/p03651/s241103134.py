N,K = map(int, input().split())
A = [int(a) for a in input().split()]

L = sorted(A)
while N > 1:
    s = set()
    for i in range(len(L)-1):
        s.add(L[i+1]-L[i])
    L = list(s)
    L.sort()
    if L[0] == 1 or len(L) == 1:
        break

if K > max(A):
    ans = "IMPOSSIBLE"
elif K in A or L[0] == 1:
    ans = "POSSIBLE"
else:
    ans = "IMPOSSIBLE"
    for a in A:
        if a-K < 0:
            continue
        if (a-K)%L[0] == 0:
            ans = "POSSIBLE"
            break

print(ans)