N,A,B = map(int, input().split())
H = [int(input()) for _ in range(N)]

def f(n):
    cnt = 0
    flag = True
    for h in H:
        x = (h-B*n)//(A-B) + min((h-B*n)%(A-B), 1)
        cnt += max(0, x)
    if cnt <= n:
        return True
    else:
        return False
        
l = 0
r = 10**9
while r-l > 1:
    m = (r+l)//2
    if f(m):
        r = m
    else:
        l = m
        
if f(l):
    print(l)
else:
    print(r)