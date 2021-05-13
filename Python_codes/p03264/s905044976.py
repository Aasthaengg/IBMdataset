import math
def main():
    K = int(input())
    if K % 2 == 0:
        print(K**2//4)
    else:
        print(math.floor(K//2)*(math.floor(K//2)+1))
if __name__ == "__main__":
    main()