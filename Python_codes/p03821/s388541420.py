import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = []; B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    ans = 0
    for i in range(N):
        a = A.pop()
        b = B.pop()
        if (a + ans)%b == 0:
            continue
        else:
            ans += b - (a + ans)%b
    print(ans)

if __name__ == "__main__":
    main()
