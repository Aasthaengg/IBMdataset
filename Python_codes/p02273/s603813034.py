n= int(input())
def koch(s,t,n):
    if n==0: #何回思考を繰り返したかを示す変数
        pass
    else:
        x= (t[0]-s[0])/3  # (x,y)は端点を結ぶ線分を三等分した時のベクトル
        y= (t[1]-s[1])/3
        ss= [ s[0]+ x, s[1]+ y ]  #ssはs,tの三等分点のうち、s寄りの点
        tt= [ t[0]- x, t[1]- y ]  #ttはs,tの三等分点のうち、t寄りの点
        st= [ ss[0]+ x/2- (3**0.5)*y/2 , ss[1]+ (3**0.5)*x/2+ y/2 ] #stは三角形の頂点の座標
        
        koch(s,ss,n-1) #1/3線分で再帰。nの値を１減らす
        print(ss[0],ss[1])  #点の座標を表示
        koch(ss,st,n-1)
        print(st[0],st[1])
        koch(st,tt,n-1)
        print(tt[0],tt[1])
        koch(tt,t,n-1)
    


print(0,0)
koch([0,0],[100,0],n)
print(100,0)
    



