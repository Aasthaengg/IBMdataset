n = int(input())
a = list(map(int, input().split()))

def chk(a,t):     # t=True(奇数項が正), t=False(偶数項が正) 
    cnt=0   # 操作回数
    x=0     # 塁積和        
    for i in a:
        x+=i      
        if t==True and x<=0:       # 正項予定なのに累積が負か0
            cnt+=1-x                              
            x=x+(1-x)               # 今回のcntで符号変更
        elif t==False and x>=0:   # 負項予定なのに累積が正か0
            cnt+=1+x              
            x=x-(1+x)              # 今回のcntで符号変換
        t = not t                  # 次の項は符号が逆
    return cnt

print(min(chk(a,True),chk(a,False)))