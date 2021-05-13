import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    s = input()
    r = s.count('R') * s.count('G') * s.count('B')

    for i1 in range(n-2):
        for i2 in range(i1 + 1, n-1):
            k = i2 * 2 - i1
            if k < n:
                if s[i1] != s[i2] and s[i1] != s[k] and s[i2] != s[k]:
                    r -= 1
    print(r)

if __name__ == '__main__':
    main()