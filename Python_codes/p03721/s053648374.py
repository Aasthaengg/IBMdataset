import sys
rl=sys.stdin.readline

def main():
    n,k=map(int,rl().strip().split())
    ints=[list(map(int,rl().strip().split())) for _ in range(n)]
    ints.sort(key=lambda e:e[0])
    s=0
    for e in ints:
        s+=e[1]
        if s>=k:
            print(e[0])
            break

if __name__=='__main__':
    main()
