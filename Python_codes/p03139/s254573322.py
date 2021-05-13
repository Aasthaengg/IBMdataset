n,a,b = list(map(int,input().split()))

if(a+b <= n):
    print(str(min(a,b)) + " 0")
else:
    print(str(min(a,b)) + " " + str(abs(a+b-n)))