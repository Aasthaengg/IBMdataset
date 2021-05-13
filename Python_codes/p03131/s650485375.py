K,A,B = map(int,input().split())
ans = 0
if B-A <= 2:
    # 1円に交換せず割り続けたほうが良い
    ans = 1+K
else:
    # x 回 ビスケット→円→ビスケットが行われると
    # ビスケットの儲けは(B-A)*2,消費する手数はx*2
    # k-x*2 分は交換せず叩いて増やす
    x = max(0,(K-(A-1))//2)
    ans = 1 + (B-A)*x + (K-(x*2))
print (ans)