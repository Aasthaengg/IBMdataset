#全国統一プログラミング王決定戦予選 a
n,a,b=map(int,input().split())
ans1=min(a,b)
ans2=max(0,a+b-n)
print(ans1,ans2)