import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, l = MI()
    ans = 0
    temp = l
    for i in range(n):
        ans += l+i
        if abs(temp) > abs(l+i):
            temp = l+i
        
    ans -= temp
    print(ans)

if __name__ == '__main__':
    main()