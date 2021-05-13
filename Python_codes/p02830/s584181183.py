import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    S, T = map(list, input().split())
    str = ''
    for s, t in zip(S, T):
        str += (s + t)
    print(str)

if __name__ == '__main__':
    main()