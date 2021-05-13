import sys
def IL(): return map(int,sys.stdin.readline().rstrip().split())

if __name__=='__main__':
    x,y = IL()
    if x==y:
        print(-1)
        exit()
    for rep in range(x,10**9+1,x):
        if rep%y!=0:
            print(rep)
            exit()
    print(-1)
    exit()