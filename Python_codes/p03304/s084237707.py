def LI(): return list(map(int, input().split()))
n, m, d = LI()
if d == 0:
    one = n
    two = 0
else:
    hidari = d - max(0, 2*d-n)
    migi = n-hidari

    one = hidari*2
    two = max(0, migi - hidari)
    #print(hidari, migi,one,two)
a = one + 2*two
ans = (a*(m-1))/n**2
print(ans)

