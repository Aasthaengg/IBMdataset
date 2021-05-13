import sys
def main():
    a,b,x=tuple(map(int,sys.stdin.readline().split()))
    res=b//x-a//x if a%x!=0 else b//x-a//x+1
    print(res)
if __name__=='__main__':main()