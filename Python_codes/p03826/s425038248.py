import sys
readline = sys.stdin.buffer.readline

a,b,c,d = map(int,readline().split())

class Square():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def require(self,ab_or_cd=0):
        if ab_or_cd==0:
            return self.a * self.b
        else:
            return self.c * self.d
    
    def compare(self):
        print(self.require(0) if self.require(0) >= self.require(1) \
            else self.require(1))

x = Square(a,b,c,d)
x.compare()


