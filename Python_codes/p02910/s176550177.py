import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = list(input())
    for i in range(len(s)):
        if s[i] == 'U' or s[i] == 'D':
            pass
        elif i % 2 == 0 and s[i] == 'R':
            pass
        elif i % 2 == 1 and s[i] == 'L':
            pass
        else:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()