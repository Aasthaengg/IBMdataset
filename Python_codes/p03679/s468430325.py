x,a,b = list(map(int, input().split()))

if b > a+x:
    print('dangerous')
elif a < b <= a+x:
    print('safe')
else:
    print('delicious')