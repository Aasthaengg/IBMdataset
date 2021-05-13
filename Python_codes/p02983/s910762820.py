import sys

def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))

def Main():
    l, r = read_ints()
    ans = 2020
    if r - l >= 2019:
        print(0)
        exit()
    for i in range(l, r + 1):
        for j in range(l, i):
            ans = min(ans, i * j % 2019)
    print(ans)

if __name__ == '__main__':
    Main()
