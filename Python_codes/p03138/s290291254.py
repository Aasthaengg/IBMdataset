n,k = map(int, input().split( ))
a = list(map(int, input().split( )))
l = max(max(a),k).bit_length()###
x = 0
ans = 0
flag = False#既にx<kが確定しているか否か,ループ内だとおかしい
for i in range(l-1,-1,-1):
    cnt = 0
    
    for j in range(n):#i bit目に1が立っている数を数える
        cnt += a[j]>>i&1
    if (k>>i&1 or flag) and cnt<n-cnt:#i bit目に1が立てられてかつ立てたほうが良い
        x += 1<<i
        ans += (n-cnt)*(1<<i)
    else:
        ans += cnt*(1<<i)
    if (k>>i)>(x>>i):
        flag = True
print(ans)
