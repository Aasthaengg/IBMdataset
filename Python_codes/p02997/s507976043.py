import sys
def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    num = (N-1)*(N-2)//2
    if K > num:
        print(-1)
        return
    ans = []
    for i in range(2, N+1):
        ans.append((1, i))
    for i in range(2, N+1):
        for j in range(i+1, N+1):
            if num == K: break
            ans.append((i, j))
            num -= 1
    print(len(ans))
    for u, v in ans:
        print(u, v)

if __name__ == '__main__':
    main()