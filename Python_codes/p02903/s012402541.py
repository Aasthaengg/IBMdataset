import sys
#input = sys.stdin.buffer.readline

def main():
    H,W,A,B = map(int,input().split())
    u = ["0" for _ in range(A)] + ["1" for _ in range(W-A)]
    _u = ["1" for _ in range(A)] + ["0" for _ in range(W-A)]
    
    for _ in range(B):
        print("".join(u))
    for _ in range(H-B):
        print("".join(_u))

if __name__ == "__main__":
    main()
