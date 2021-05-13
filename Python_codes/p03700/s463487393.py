n, a, b = map(int,input().split())
ad = a - b
H = [int(input()) for i in range(n)]

le = 0
ri = max(H) // b + 2
mid = (le + ri) // 2
while ri - le > 1:
    ad_n = 0
    for i in range(n):
        hh = max(0, H[i] - mid * b)
        #print(H[i])
        ad_n += -(-hh // ad)
    #print(ad_n, mid)
    if ad_n > mid:  # 倒せない
        le = mid
    else:
        ri = mid
    mid = (le + ri) // 2
print(le+1)
