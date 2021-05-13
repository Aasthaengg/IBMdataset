n = int(input())
A = list(map(int, input().split()))
A.sort()
u, d = A[-1], A[0]
print(sum(abs(a) for a in A) - 2*min(abs(u), abs(d))*int(u*d>0))
for a in A[1:-1]:
    if a<0:
        print(u, a)
        u -= a
    else:
        print(d, a)
        d -= a
print(u, d)