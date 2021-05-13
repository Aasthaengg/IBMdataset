import sys
x,n=map(int,input().split())
p=list(map(int,input().split()))

if n==0:
    print(x)
else:
    q=[abs(p[i]-x) for i in range(n)]
    re=max(q) #xと最も離れているものはどれだけ離れてるか
    i=0
    if re==0:
        print(x-1)
    else:
        while(i < re+1):
            if x-i not in p:
                print(x-i)
                break
            elif x+i not in p:
                print(x+i)
                break
            i += 1
        if i==re+1:
            print(x-i)