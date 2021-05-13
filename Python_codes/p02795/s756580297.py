import math
def main():
    H = int(input())
    W = int(input())
    N = int(input())
    print(int(math.ceil(N/max(H, W))))
    
if __name__ == "__main__":
    main()