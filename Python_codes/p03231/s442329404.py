def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
N,M = map(int,input().split())
S = input().strip()
T = input().strip()
a = gcd(N,M)
K = (N//a)*M
t = (N//a)*(M//a)
flag = 0
k = 0
while (k*t)//(K//N)<N and (k*t)//(K//M)<M:
    if S[(k*t)//(K//N)]!=T[(k*t)//(K//M)]:
        flag = 1
        break
    k += 1
if flag==0:
    print(K)
else:
    print(-1)