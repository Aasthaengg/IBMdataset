import math
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(math.ceil((n-k)/(k-1)+1))
    
if __name__ == "__main__":
    main()