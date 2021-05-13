k, t = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
if t == 1:
    print(k-1)
    exit()

x = A[0]
s = sum(A)-A[0]
if s >= x:
    print(0)
else:
    ans = x-s-1
    print(max(ans, 0))
