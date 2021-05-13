x,a,b = map(int,input().split())
if -a + b <= 0:
    print("delicious")
elif 0 < -a + b < x+1:
    print("safe")
elif -a + b >= x+1:
    print("dangerous")