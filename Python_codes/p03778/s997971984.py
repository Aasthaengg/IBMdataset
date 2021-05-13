W,a,b = map(int,input().split())
if b>a :
    if (W+a)>=b :
        print(0)
    elif b>(W+a) :
        print(b-(W+a))
elif a==b :
    print(0)
else :
    if (W+b)>=a :
        print(0)
    elif a>(W+b) :
        print(a-(W+b))