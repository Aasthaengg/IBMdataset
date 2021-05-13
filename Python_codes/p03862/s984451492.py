import sys
def main():
    N,x=tuple(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    pa,r=0,0
    for a in A:
        c=a+pa-x
        if c>0:
            r+=c
            pa=a-c
        else:pa=a
    print(r)
if __name__=='__main__':main()