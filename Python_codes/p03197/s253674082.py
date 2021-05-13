import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    b = False
    for _ in range(N):
        if int(input())%2 != 0:
            b = True
            break
            
    if b:
        print("first")
    else:
        print("second")

if __name__ == "__main__":
    main()
