n,h,w = map(int,input().split())
a = []
b = []
for i in range(n):
    A,B = map(int,input().split())
    a.append(A)
    b.append(B)
ans = 0
for i in range(n):
    if a[i] >= h and b[i] >= w:
        ans += 1
print(ans)