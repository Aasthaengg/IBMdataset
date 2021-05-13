n=int(input())
ans=0
if n % 2==0:
    for i in range(1,10000):
        waru = 2*5**i
        if n < waru:
            break
        else:
            tmp = n//waru
            ans += tmp
print(str(ans))