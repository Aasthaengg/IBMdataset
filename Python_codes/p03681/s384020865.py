p = 10**9+7
N,M = map(int,input().split())
a = 1
for i in range(2,N+1):
    a = (a*i)%p
b = 1
for i in range(2,M+1):
    b = (b*i)%p
if M==N:
    n = (2*a*b)%p
elif M==N-1 or N==M-1:
    n = (a*b)%p
else:
    n = 0
print(n)