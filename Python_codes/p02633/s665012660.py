import math

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    X = ii()
    for i in range(1, 361):
        if (X*i)%360==0:
            print(i)
            return

if __name__ == '__main__':
    main()