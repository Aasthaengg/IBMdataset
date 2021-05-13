import sys

input = sys.stdin.readline

def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        diff = t[i+1] - t[i]
        ans += (diff<T)*(diff) + (diff>=T)*T
    ans += T
    print(ans)

if __name__ == "__main__":
    main()       
