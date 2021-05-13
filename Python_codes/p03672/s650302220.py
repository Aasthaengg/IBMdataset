import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    s = input()
    len_s = len(s)
    for i in range(2, len_s-1, 2):
        len_s -= 2
        left = s[:len_s//2]
        right = s[len_s//2:len_s]
        if left == right:
            break
    print(len_s)

if __name__ == '__main__':
    main()