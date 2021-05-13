def comb(n,r):
    if n < r:
        return 0
    si,bo = 1,1
    for i in range(n):
        si *= i+1
    for i in range(r):
        bo *= i+1
    for i in range(n-r):
        bo *= i+1
    return si//bo

N,A,B = map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse=True)

print(sum(v[:A])/A)
n = 0
r = 0
for i in range(A):
    if v[i] == v[A-1]:
        r += 1
        n += 1
for i in range(A,N):
    if v[i] == v[A-1]:
        n += 1
ans = 0
if v[0] != v[A-1]:
    print(comb(n,r))
    exit()
for _ in range(A,B+1):
    ans += comb(n,r)
    r += 1
print(ans)
