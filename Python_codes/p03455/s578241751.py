#import sys

def main():
    #args = sys.argv
    a, b = map(int, input().split())
    residual = ( a * b )%2
    if residual == 1:
        print("Odd")
    else :
        print("Even")

if __name__ == "__main__":
    main()