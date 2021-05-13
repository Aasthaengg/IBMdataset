x,a,b=map(int,input().split())
ans=['delicious','safe','dangerous']

if b-a<=0:
    print(ans[0])
elif b-a<=x:
    print(ans[1])
elif b-a>x:
    print(ans[2])