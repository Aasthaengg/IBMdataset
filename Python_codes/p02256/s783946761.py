from collections import defaultdict

def gcd(x,y):
    if max(x,y) % min(x,y) == 0 : return min(x,y)
    else : return gcd(min(x,y) ,max(x,y)%min(x,y))

if __name__ == '__main__' :
        a,b = [int(i) for i in input().split(" ")]
        print(gcd(a,b))
