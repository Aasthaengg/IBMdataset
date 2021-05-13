k,a,b=map(int,input().split())
ans=1
if b-a<=2: #交換するメリットがない k回すべて一枚増やす
    print(ans+k)
else:
    if k<(a+1):
        print(ans+k)
    else:
        zan=(k-(a-1))
        if zan%2==0:
            print(max(ans+k,a+(zan//2)*(b-a)))
        else:
            print(max(ans+k,a+(zan//2)*(b-a)+1))