import sys
input = sys.stdin.readline

def main():
    N = int(input())
    if N == 3:
        print(2)
        print(1,3)
        print(2,3)
    elif N == 4:
        print(4)
        print(1,2)
        print(1,3)
        print(4,2)
        print(4,3)
    else:
        if N%2 == 0:
            print(N*2)
            for i in range(N//2-1):
                print(i+1,i+2)
                print(i+1,N-i-1)
                print(N-i,i+2)
                print(N-i,N-i-1)
            for i in range(2):
                print(N//2+i,1)
                print(N//2+i,N)
        else:
            print(N*2-2)
            for i in range(N//2-1):
                print(i+1,i+2)
                print(i+1,N-i-2)
                print(N-i-1,i+2)
                print(N-i-1,N-i-2)
            print(N//2,N)
            print(N//2+1,N)
            print(N,1)
            print(N,N-1)

if __name__ == "__main__":
    main()