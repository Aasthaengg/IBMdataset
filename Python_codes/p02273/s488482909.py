import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,a):
        return self.__class__(self.x+a.x,self.y+a.y)

    def __sub__(self,a):
        return self.__class__(self.x-a.x,self.y-a.y)

    def __mul__(self,d):
        return self.__class__(self.x*d,self.y*d)

    def __truediv__(self,d):
        return self.__class__(self.x/d,self.y/d)

    def __str__(self):
        return '%.10f %.10f'%(self.x,self.y)

    def abs(self):
        return (self.x*self.x+self.y*self.y)**(1.0/2.0)

    def rotate(self,d):
        r = math.pi*d/180.0
        return self.__class__( self.x*math.cos(r)-self.y*math.sin(r),
                               self.x*math.sin(r)+self.y*math.cos(r))

def func(p1,p2,n):

    if n==0:return

    v = (p2-p1)
    a = p1+v/3.0
    c = p1+v*2.0/3.0
    b = a+(c-a).rotate(60.0)

    func(p1,a,n-1)
    print (a)
    func(a,b,n-1)
    print (b)
    func(b,c,n-1)
    print (c)
    func(c,p2,n-1)

def main():
    n = int(input())
    a = Point(0.0,0.0)
    b = Point(100.0,0.0)
    print (a)
    func(a,b,n)
    print (b)

if __name__ == '__main__':
    main()


