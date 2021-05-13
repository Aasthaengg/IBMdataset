n,k = map(int,input().split())
a = [int(i) for i in input().split()]

b = a.index(1) 
ans = 0
b -= (k-1)
if b < 0:
    b = a.index(1) + abs(b)
if b > n-1 -(k-1):
    b -= b- (k-1)
c,d = divmod(b,k-1)
ans += c
if d != 0:
    ans +=1
e,f = divmod(n-1 - b,k-1)
ans += e
if f != 0:
    ans +=1
if d != 0 and f != 0 and d + f <= k-1:
    ans -=1
print(ans)