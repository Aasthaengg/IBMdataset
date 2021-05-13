import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    a, b, c = MI()
    if a%2 or b%2 or c%2:
        print(0)
        sys.exit()
    if (a == b) and (b == c):
        print(-1)
        sys.exit()
    cnt = 0
    while True:
        if a%2 or b%2 or c%2:
            break
        temp_a = a
        temp_b = b
        temp_c = c
        a = temp_b//2 + temp_c//2
        b = temp_a//2 + temp_c//2
        c = temp_a//2 + temp_b//2
        cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()