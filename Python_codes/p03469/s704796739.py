import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input().split('/')
    s[0] = '2018'
    print('/'.join(s))

if __name__ == '__main__':
    main()