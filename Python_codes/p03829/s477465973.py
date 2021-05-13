import sys

def main():
    N,A,B=map(int,input().split())
    towns=list(map(int,sys.stdin.readline().strip().split()))
    f=lambda x:min(A*x,B)
    fl=0
    for x in range(N-1):
        fl+=f(towns[x+1]-towns[x])
    print(fl)

if __name__=='__main__':
    main()

