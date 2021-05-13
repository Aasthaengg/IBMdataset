a,b,c = map(int,input().split())
if (a%2==0)or(b%2==0)or(c%2==0):
    print(0)
else:
    x = [a,b,c]
    x.sort()
    print(x[0]*x[1])