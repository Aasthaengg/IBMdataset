import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    d = int(input())
    s = " Eve"
    print("Christmas" + s*(25-d))
            
if __name__ == '__main__':
    main()