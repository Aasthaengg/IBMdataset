K=int(input())
*A, = map(int,input().split())
m,M = 2,2
for a in A[::-1]:
    M = M//a*a+(a-1)
    m = ((m-1)//a+1)*a
    if m>M:
        print(-1)
        break
else:print(m,M)