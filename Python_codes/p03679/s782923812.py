import sys
input = sys.stdin.readline

x,a,b = list(map(int,input().split()))
if -a+b<=0:
    print('delicious')
elif 0<-a+b<=x:
    print('safe')
else:
    print('dangerous')