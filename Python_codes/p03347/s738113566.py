import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = int(input())
    if a != 0:
        print(-1)
        return
    ans = 0
    flag = False
    for _ in range(N-1):
        tmp = int(input())
        if tmp == a + 1:
            ans += tmp
            ans -= a
        elif tmp < a + 1:
            ans += tmp
        else:
            print(-1)
            return
        a = tmp
    print(ans)    

if __name__ == "__main__":
    main()
