import math
def main():
    n,k=map(int,input().split())
    print(math.ceil(n/k-n//k))
    
if __name__ == "__main__":
    main()