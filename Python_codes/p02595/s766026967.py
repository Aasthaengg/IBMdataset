import math
if __name__ == "__main__":
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        d = math.sqrt(x*x + y*y)
        if d <= D:
            ans += 1
    print(ans)