import sys
def main():
    input = sys.stdin.readline
    N=int(input())
    Nd=set()
    for n in range(1,int(N**0.5)+1):
        if N%n==0:
            Nd.add(n)
            Nd.add(N//n)
    N1d=set()
    for n in range(1,int((N-1)**0.5)+1):
        if (N-1)%n==0:
            N1d.add(n)
            N1d.add((N-1)//n)
    for d in Nd:
        if d==1: continue
        n=N
        while n%d==0: n//=d
        if n%d==1: N1d.add(d)
    print(len(N1d)-1)

if __name__ == '__main__':
    main()
