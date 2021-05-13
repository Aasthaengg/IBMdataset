N,L = map(int,input().split())
a = N*L+(N*(N-1))//2
d = 1000
ans = -1000
for i in range(L,L+N):
    b = a-i
    if abs(a-b)<d:
        d = abs(a-b)
        ans = b
print(ans)