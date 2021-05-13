import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    s = input()
    k = I()
    for i, si in enumerate(s):
        if si != '1':
            print(si)
            sys.exit()
        if i == k-1:
            break
    print(1)

if __name__ == '__main__':
    main()