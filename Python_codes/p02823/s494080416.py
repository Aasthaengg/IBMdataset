n,a,b = map(int, input().split())
d = b - a
if d%2==0: ans = d//2 # AB間偶数
else: ans = min(a, n-b+1) + (d-1)//2 # 端寄せを一回多く行えば AB間が１つ詰まって偶数
print(ans)
