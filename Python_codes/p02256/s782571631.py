x,y = map(int,input().split())

def swap(x,y):
    temp = x
    x = y
    y = temp
    return(x,y)

def gcd(x,y):
    if x < y:
        x,y= swap(x,y)

    while(x != y and y != 0):
        x = x%y
        x,y = swap(x,y)
    print(x)

gcd(x,y)

