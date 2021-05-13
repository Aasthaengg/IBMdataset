n = int(input())
a = list(map(int,input().split()))

tot = sum(a)
ans = -1
dif = 10**6
for i,ai in enumerate(a):
    dif_i = abs(ai*n - tot)
    if(dif > dif_i):
        dif = dif_i
        ans = i
print(ans)