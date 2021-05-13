x,k,d=[int(i) for i in input().strip().split(" ")]
#絶対値変換
x=abs(x) if x<0 else x
#減らすのみ
if x//d>=k:
    print(x-d*k)
else:
    if (k-x//d)%2==0:
        print(x%d)
    else:
        print(d-(x%d))