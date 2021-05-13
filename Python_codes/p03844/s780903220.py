import sys
readline = sys.stdin.buffer.readline

a,op,b = readline().rstrip().decode('utf-8').split()

class Input():
    def __init__(self,a,op,c):
        self.a = int(a)
        self.b = int(b)
        self.op = op

class Calc(Input):
    def __call__(self):
        if self.op == "+":
            return self.a+self.b
        else:
            return self.a-self.b

x = Calc(a,op,b)
print(x())