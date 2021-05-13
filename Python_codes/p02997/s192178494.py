import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())

    tmp = ((N-1)*(N-2)) // 2
    if K > tmp:
        print(-1)
        return
    ans = [(1, i) for i in range(2, N+1)]
    count = tmp - K
    if count > 0:
        for i in range(2, N+1):
            for j in range(i+1, N+1):
                ans.append((i, j))
                count -= 1
                if count == 0:
                    break
            if count == 0:
                break
    
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


if __name__ == "__main__":
    main()