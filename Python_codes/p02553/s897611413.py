a,b,c,d=map(int,input().split())
ans=[a*c,a*d,b*c,b*d]
if a<=0<=b or c<=0<=d:
    print(max(max(ans),0))
else:
    print(max(ans))