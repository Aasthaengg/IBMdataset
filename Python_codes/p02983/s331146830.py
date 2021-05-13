import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    mod  =2019
    L,R = map(int,input().split())
    if R //mod - (L-1) //mod >1:
        print(0)
        exit()
    ans = 10**9
    for i in range(L,R):
        for j in range(i+1,R+1):
            a = (i * j ) %mod
            ans = min(a,ans)
    print(ans)



if __name__ == "__main__":
    main()
