from collections import deque

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = deque(a)
    ans = 0
    for i in range(N):
        a.pop()
        ans += a.pop()
        a.popleft()
    print(ans)

if __name__ == "__main__":
    main()
