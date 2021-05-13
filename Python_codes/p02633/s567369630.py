def g(a,b):
    if a*b:
        if a>b:
            return g(a-b,b)
        elif(a<b):
            return g(a,b-a)
        else:
            return a
    else:
        if(a*b):
            return max(a,b)
        else:
            return 1
n=int(input())
print(360//g(n,360))