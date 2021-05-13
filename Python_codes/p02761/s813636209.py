n,m = map(int,input().split())
if m == 0 and n != 1:
    print(10**(n-1))
    exit()
if m== 0 and n==1:
    print(0)
    exit()
l = [-1]*n
for i in range(m):
    s,c = map(int,input().split())
    if l[s-1] == -1:
        l[s-1] = c
    elif l[s-1] != c:
        print('-1')
        exit()
if l[0] == 0 and n==1:
    print(0)
    exit()
if l[0] == 0:
    print('-1')
    exit()
if l[0] == -1:
    l[0] = 1
for i in range(1,n):
    if l[i] == -1:
        l[i] = 0
# print(l)
ans = 0
for i in range(n):
    ans += l[n-i-1]*10**i
print(ans)