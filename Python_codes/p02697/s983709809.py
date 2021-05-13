def main():
    N, M = map(int, input().split())
    ans = []
    if N%2:
        for l in range(1, N//2+1):
            r = N-l
            ans.append([l,r])
    else:
        for l in range(1, N//2+1):
            r = N-l+1
            if l>N//4:
                r -= 1
            ans.append([l,r])
    for i in range(M):
        print(ans[i][0], ans[i][1])
    return
main()