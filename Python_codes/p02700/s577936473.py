import math
def resolve():
    a,b,c,d = map(int,input().split())
    A = math.ceil(c/b)
    B = math.ceil(a/d)
    print('Yes' if A <= B else 'No')
resolve()