import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline

def main():
    a,b,c = read().split('/')
    if a == '2017':
        a = '2018'
    print("{}/{}/{}".format(a,b,c))

if __name__ == '__main__':
    main()
