import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _, _, X, Y = map(int, input().split())
    max_x = max(map(int, input().split() + [X]))
    min_y = min(map(int, input().split() + [Y]))

    if max_x < min_y:
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()
