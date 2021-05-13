import sys

def input():
    return sys.stdin.readline()

def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))
    kaishi = 0
    syuuryou = 0
    time = 0
    for i in t:
        if syuuryou < i:
            time += syuuryou - kaishi
            kaishi = i
        syuuryou = i + T
    time += syuuryou - kaishi 
    print(time)
    
if __name__ == "__main__":
    main()