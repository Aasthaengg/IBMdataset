a,b = [int(x) for x in input().split()]
if any([a%3==0,b%3==0,(a+b)%3==0]):
    print("Possible")
else:
    print("Impossible")