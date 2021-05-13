import bisect
A, B, Q = map(int, input().split())

a=[-float("inf")]
b=[-float("inf")]
for i in range(A):
    a.append(int(input()))
for i in range(B):
    b.append(int(input()))   
a+=[float("inf")]
b+=[float("inf")]

for i in range(Q):
    q = int(input())
    x = bisect.bisect_left(a, q)
    y = bisect.bisect_left(b, q)
    ans = float("inf")
    for j in [a[x-1], a[x]]:
        for k in [b[y-1], b[y]]:
            ans1 = abs(j-q)+abs(j-k)
            ans2 = abs(k-q)+abs(j-k)
            ans = min(ans, ans1, ans2)
    print(ans)