import collections

N = int(input())
l = list(map(int,input().split()))

c = collections.Counter(l)
ans = 0
flag = True
if N%2==0:
    for i in range(1,N+1,2):
        if c[i] != 2:
            flag = False
else:
    for i in range(0,N+1,2):
        if i == 0 and c[i] != 1:
            flag = False 
        if i != 0 and c[i] != 2: 
            flag = False

if flag:
    ans = 2**int(N/2)
print(ans % (10**9+7))