import sys

def main():
    N = int(input())
    zoro = 0
    for i in range(N):
        Ds = [int(s) for s in sys.stdin.readline().split()]
        if(Ds[0] == Ds[1]):
            zoro += 1
            if(zoro > 2):
                print("Yes")
                return(0)
        else:
            zoro = 0
    print("No")

main()