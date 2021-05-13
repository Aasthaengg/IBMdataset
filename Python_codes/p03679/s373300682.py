x,a,b=map(int, input().split())
ans = 0 - a
ans += b
if ans > x:
    print('dangerous')
elif ans <= 0:
    print('delicious')
else:
    print('safe')
