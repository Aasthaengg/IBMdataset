import sys
def v():
    a,b,c=tuple(map(int,sys.stdin.readline().split()))
    if any([a==b+c,b==c+a,c==a+b]):print('Yes')
    else:print('No')
if __name__=='__main__':v()
