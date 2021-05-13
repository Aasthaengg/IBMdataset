a,b,c = map(int,input().split())
res = 0
while a%2==0 and b%2==0 and c%2==0: # 値が偶数の間
    if a==b==c: #無限ループ
        print(-1)
        exit()
    tmpa = b//2+c//2
    tmpb = a//2+c//2
    tmpc = a//2+b//2
    a = tmpa
    b = tmpb
    c = tmpc
    res += 1
print(res)