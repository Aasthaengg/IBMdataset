n = int(input())
a = list(map(int,input().split()))
ans = 0

uf,df = True,True
x = a[0]
for ai in a:
    
    if x > ai:
        uf = False
    if x < ai:
        df = False
    if (uf or df) is False:
        ans += 1
        uf,df, = True,True
    x = ai
print(ans+1)