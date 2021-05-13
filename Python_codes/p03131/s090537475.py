import sys
input = sys.stdin.buffer.readline

def main():
    K,A,B = map(int,input().split())
    if A+2 >= B:
        print(K+1)
    else:
        if K<=A:
            print(K+1)
        else:
            rest = K-(A-1)
            print(A+(B-A)*(rest//2)+rest%2)
    
if __name__ == "__main__":
    main()
