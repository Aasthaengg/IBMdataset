# 一番左はX
# X,2X,4X,8X...とつづく
# a0=X,a1=2**1*X,a2=2**2*X...ai=2**i*X
# ai<=Yをみたす最大のiがしりたい
# 答えはi+1?
x,y=map(int,input().split())
for i in range(100):
  if pow(2,i)*x>y:
    break
print(i)