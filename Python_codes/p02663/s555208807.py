h,m,hh,mm,k = map(int,input().split())
bi = h*60 + m
en = hh*60 +mm
print(max(en - bi - k,0))
